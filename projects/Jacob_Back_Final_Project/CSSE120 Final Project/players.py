import mqtt_remote_method_calls as com


class Player(object):
    """Creates and stores the instance variables for the Player class. """
    def __init__(self, rectangle, canvas, idp, canvas_power_up, power_rect,
                 player_score):
        self.speed = 20
        self.r_speed = 500
        self.id = idp
        self.rectangle = rectangle
        self.canvas = canvas
        self.top_maximum = 0
        self.bottom_maximum = 400
        self.score = 0
        self.power_up = False
        self.power_up_canvas = canvas_power_up
        self.power_up_rect = power_rect
        self.player_score = player_score
        self.mqtt_client_robot = com.MqttClient(self)
        if self.id == 1:
            self.mqtt_client_robot.connect_to_ev3()
        else:
            self.mqtt_client_robot.connect_to_ev3(lego_robot_number=400)
        self.mqtt_client_one = com.MqttClient(None)
        self.mqtt_client_one.connect_to_mover()

    def move_up(self):
        """"Moves the rectangle upward until the top of the canvas is
            reached and sends its current position to the mover.py file and
            to the robot using mqtt communication """
        if self.canvas.coords(self.rectangle)[1] >= \
                        self.top_maximum + self.speed:
            self.canvas.move(self.rectangle, 0, -self.speed)
            self.mqtt_client_one.send_message('update_rectangle',
                                              [self.canvas.coords(
                                                  self.rectangle), self.id])
            self.mqtt_client_robot.send_message('drive_inches', [1,
                                                                 self.r_speed])

    def move_down(self):
        """"Moves the rectangle downward until the bottom of the canvas is
            reached and sends its current position to the mover.py file and
            to the robot using mqtt communication """
        if self.canvas.coords(self.rectangle)[3] <= \
                        self.bottom_maximum - self.speed:
            self.canvas.move(self.rectangle, 0, 10)
            self.mqtt_client_one.send_message('update_rectangle',
                                              [self.canvas.coords(
                                                  self.rectangle), self.id])
            self.mqtt_client_robot.send_message('drive_inches', [-1,
                                                                 self.r_speed])

    def power_up_avialable(self):
        """Calls the robots function power_up_avialable"""
        self.power_up = self.mqtt_client_robot.send_message(
            'power_up_avialable', [])

    def change_power_up_state(self):
        """Changes the state of self.power_up to True and changes the color
        of the power up rectangle to green"""
        self.power_up = True
        self.power_up_canvas.itemconfig(self.power_up_rect, fill='green')

    def call_for_power_up(self):
        """Tells the robot to get the current color it is over"""
        self.mqtt_client_robot.send_message('get_color_value', [])

    def get_power_up(self, color):
        """Determines the robot and player's speed based upon the color
        passed into the method. Then, sets self.power_up to False, changes
        the powerup rectangle color back to red, and sends a meessage over
        mqtt communication for the robot to lower its arm."""
        if self.power_up:
            print(color)
            if color < 5:
                self.speed = 10
                self.r_speed = 400
            elif color < 10:
                self.speed = 15
                self.r_speed = 450
            elif color < 20:
                self.speed = 20
                self.r_speed = 500
            elif color < 80:
                self.speed = 25
                self.r_speed = 550
            else:
                self.speed = 30
                self.r_speed = 600
        self.power_up = False
        self.power_up_canvas.itemconfig(self.power_up_rect, fill='red')
        self.mqtt_client_robot.send_message('arm_down', [])

    def update_score(self):
        """Updates the players scoreboard"""
        self.player_score.delete(0, len(self.player_score.get()))
        self.score = self.score + 1
        self.player_score.insert(0, str(self.score))


class Ball(object):
    def __init__(self, circle, canvas):
        """Creates and stores the instance variables for the Ball class."""
        self.circle = circle
        self.canvas = canvas
        self.mqtt_client_one = com.MqttClient(None)
        self.mqtt_client_one.connect_to_mover()

    def update_position(self, dx, dy):
        """Changes the position of the ball and sends its position to the
        mover.py file."""
        self.canvas.move(self.circle, dx, dy)
        self.mqtt_client_one.send_message("update_circle",
                                          [self.canvas.coords(self.circle)])
