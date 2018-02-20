import mqtt_remote_method_calls as com
import math
import time


class MyDelegate(object):
    def __init__(self):
        """Intializes the instances variables
            Variables set:
            self.rectangle_one
            self.rectangle_two
            self.ball
            self.original_x
            self.original_y
            self.mqtt_client
            self.run
            """
        self.rectangle_one = None
        self.rectangle_two = None
        self.ball = None
        self.original_x = 200
        self.original_y = 200
        self.mqtt_client = com.MqttClient()
        self.mqtt_client.connent_to_pc_gui()
        self.run = True

    def update(self, rect1, rect2, circle):
        """Updates self.rectangle_one, self.rectangle_two, and self.ball"""
        self.rectangle_one = rect1
        self.rectangle_two = rect2
        if circle is not None:
            self.ball = circle

    def update_circle(self, circle):
        """updates the self.circle"""
        self.ball = circle

    def update_rectangle(self, rect, num):
        """Updates one of the rectangles based upon the num passed in"""
        if num == 1:
            self.rectangle_one = rect
        else:
            self.rectangle_two = rect

    def return_to_original_position(self):
        """Places the ball at the original position it started at"""
        dx = self.original_x - (self.ball[0] + self.ball[2]) / 2
        dy = self.original_y - (self.ball[1] + self.ball[3]) / 2
        self.mqtt_client.send_message('update_position', [dx, dy])

    def stop(self):
        """Terminates the program"""
        self.run = False


def main():
    """Moves the ball on the many GUI screen based upon barriers placed
        around the rectangles and walls and increase the score when the ball
        touches one of the vertical walls."""
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connent_to_pc_gui()
    mqtt_client_player_one = com.MqttClient()
    mqtt_client_player_one.connect_to_player_one()
    mqtt_client_player_two = com.MqttClient()
    mqtt_client_player_two.connect_to_player_two()
    speed_i = 10
    speed_x = speed_i
    speed_iy = 10
    speed_y = speed_iy
    while True and my_delegate.run:
        while not (my_delegate.rectangle_one is None):
            circle_center_x = (my_delegate.ball[0] + my_delegate.ball[2]) / 2
            circle_center_y = (my_delegate.ball[1] + my_delegate.ball[3]) / 2
            if 0 + math.fabs(speed_x) + 25 < circle_center_x < (400 - speed_x
                                                                    - 25):
                if 0 + math.fabs(speed_y) < circle_center_y < (400 - speed_y):
                    mqtt_client.send_message('update_position',
                                             [speed_x, speed_y])
                    time.sleep(.25)
                elif circle_center_y > 200:
                    mqtt_client.send_message('update_position',
                                             [speed_x, 400 - circle_center_y -
                                              10])
                    speed_y = -speed_y
                elif circle_center_y < 200:
                    speed_y = speed_iy
                    time.sleep(.25)
                    mqtt_client.send_message('update_position',
                                             [speed_x, speed_y])
            elif circle_center_x > 200:
                if my_delegate.rectangle_two[1] < circle_center_y < \
                        my_delegate.rectangle_two[3]:
                    mqtt_client.send_message('update_position',
                                             [my_delegate.rectangle_two[
                                                  1] - circle_center_x - 20,
                                              speed_y])
                    print("Collison 2")
                else:
                    mqtt_client.send_message('update_position',
                                             [400 - circle_center_x - 10,
                                              speed_y])
                    mqtt_client_player_two.send_message('update_score', [])
                    mqtt_client.send_message('update_position', [-20, speed_y])
                    print("no 2")
                speed_x = -speed_x
            elif circle_center_x < 200:
                if my_delegate.rectangle_one[1] < circle_center_y < \
                        my_delegate.rectangle_one[3]:
                    mqtt_client.send_message('update_position',
                                             [my_delegate.rectangle_one[
                                                  3] - circle_center_x + 20,
                                              speed_y])
                    print("Collison 1")

                else:
                    mqtt_client.send_message('update_position',
                                             [-circle_center_x + 10, speed_y])
                    print("no 1")
                    mqtt_client_player_one.send_message('update_score', [])
                    mqtt_client.send_message('update_position', [30, speed_y])
                speed_x = speed_i
                time.sleep(.25)
                mqtt_client.send_message('update_position', [speed_x, speed_y])
            else:
                time.sleep(.25)
                mqtt_client.send_message('update_position', [0, 0])


main()
