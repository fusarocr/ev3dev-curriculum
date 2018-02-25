import ev3dev.ev3 as ev3
import time
import robot_controller as robo
import mqtt_remote_method_calls as com


class Acts_upon_messages(object):
    def __init__(self, robot):
        self.robot = robot
        pass

    def go(self):
        ev3.Sound.speak("Ha you thought.  You didn't say Simon")

    # def go_for_second_set_of_radiobuttons(self, inches, speed):
    #     if inches or speed > 0:
    #         ev3.Sound.speak("Ha you thought.  You didn't say Simon")

    def calibrate_the_arm(self):
        ev3.Sound.speak("Calibrating the arm")
        self.robot.arm_calibration()

    def move_arm_up(self):
        ev3.Sound.speak("Moving the arm up")
        self.robot.arm_up()

    def move_arm_down(self):
        ev3.Sound.speak("Moving the arm down")
        self.robot.arm_down()

    def drive_inches(self, inches, speed):
        ev3.Sound.speak("Driving inches")
        print("It went to drive inches")
        self.robot.drive_inches(inches, speed)

    def shutdown(self):
        self.robot.stop()
        print("Goodbye")
        ev3.Sound.speak("I had fun playing Simon Says").wait()

    def forward_forever(self, speed):
        ev3.Sound.speak("Moving forward")
        self.robot.left_motor.run_forever(speed_sp=speed)
        self.robot.right_motor.run_forever(speed_sp=speed)

    def backward_forever(self, speed):
        ev3.Sound.speak("Moving backward")
        self.robot.left_motor.run_forever(speed_sp=-speed)
        self.robot.right_motor.run_forever(speed_sp=-speed)

    def spin_right_forever(self, speed):
        ev3.Sound.speak("Spinning right")
        if speed == 601 or speed > 601:
            self.robot.left_motor.run_forever(speed_sp=speed - 200)
            self.robot.right_motor.run_forever(speed_sp=speed)
            print(speed)
        else:
            self.robot.left_motor.run_forever(speed_sp=speed)
            self.robot.right_motor.run_forever(speed_sp=speed + 200)

    def spin_left_forever(self, speed):
        ev3.Sound.speak("Spinning left")
        if speed == 601 or speed > 601:
            self.robot.left_motor.run_forever(speed_sp=speed)
            self.robot.right_motor.run_forever(speed_sp=speed - 200)
            print(speed)
        else:
            self.robot.left_motor.run_forever(speed_sp=speed + 200)
            self.robot.right_motor.run_forever(speed_sp=speed)

    def stop(self):
        self.robot.left_motor.run_forever(speed_sp=0)
        self.robot.right_motor.run_forever(speed_sp=0)
        ev3.Sound.speak("Simon said to stop")


def main():
    robot = robo.Snatch3r()
    robot.arm_calibration()
    ev3.Sound.speak("Ready to Play Simon Says").wait()
    acts_upon_messages = Acts_upon_messages(robot)
    send_and_receive_msg = com.MqttClient(acts_upon_messages)
    send_and_receive_msg.connect_to_pc()
    while True:
        time.sleep(0.1)
        if robot.ir_sensor.proximity < 5:
            acts_upon_messages.shutdown()
            break


main()
