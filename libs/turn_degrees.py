#     Use the run_to_rel_pos, .wait_while(ev3.Motor.STATE_RUNNING) pattern to implement your work (not timed driving)
#   You will have to experimentally determine the formula for accurate position_sp turn amounts.

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


    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        """Turns the robot left and right depending on the degrees_to_turn
        and the turn_speed_sp"""
        if degrees_to_turn > 0:
            degrees_through= degrees_to_turn
            self.left_motor.run_to_rel_pos(speed_sp=-turn_speed_sp,
                                           position_sp=degrees_through,
                                        stop_action=ev3.Motor.STOP_ACTION_BRAKE)
            self.right_motor.run_to_rel_pos(speed_sp=turn_speed_sp,
                                           position_sp=degrees_through,
                                           stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        if degrees_to_turn < 0:
            degrees_through= degrees_to_turn
            self.left_motor.run_to_rel_pos(speed_sp=turn_speed_sp,
                                           position_sp=degrees_through,
                                           stop_action=ev3.Motor.STOP_ACTION_BRAKE)
            self.right_motor.run_to_rel_pos(speed_sp=-turn_speed_sp,
                                            position_sp=degrees_through,
                                            stop_action=ev3.Motor.STOP_ACTION_BRAKE)