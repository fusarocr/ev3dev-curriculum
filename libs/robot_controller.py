"""
  Library of EV3 robot functions that are useful in many different applications. For example things

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be
        useful in many different programs."""

    def __init__(self):
        """Creates and stores left and right motor"""
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert self.left_motor.connected
        assert self.right_motor.connected

    def drive_inches(self, inches_target, speed_degree_per_second):
        """Drives robot forward by inches_target at given speed"""
        degrees_through = inches_target * 90
        self.left_motor.run_to_rel_pos(speed_sp=speed_degree_per_second,
                                       position_sp=degrees_through,
                                       stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.right_motor.run_to_rel_pos(speed_sp=speed_degree_per_second,
                                        position_sp=degrees_through,
                                        stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        """Turns the robot left and right depending on the degrees_to_turn
        and the turn_speed_sp"""
        if degrees_to_turn > 0:
            degrees_through = degrees_to_turn * 4.4375
            self.left_motor.run_to_rel_pos(speed_sp=turn_speed_sp,
                                           position_sp=-degrees_through,
                                           stop_action=ev3.Motor.STOP_ACTION_BRAKE)
            self.right_motor.run_to_rel_pos(speed_sp=turn_speed_sp,
                                            position_sp=degrees_through,
                                            stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        if degrees_to_turn < 0:
            degrees_through = degrees_to_turn * 4.4375
            self.left_motor.run_to_rel_pos(speed_sp=turn_speed_sp,
                                           position_sp=-degrees_through,
                                           stop_action=ev3.Motor.STOP_ACTION_BRAKE)
            self.right_motor.run_to_rel_pos(speed_sp=-turn_speed_sp,
                                            position_sp=degrees_through,
                                            stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
