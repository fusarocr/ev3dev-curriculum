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
import mqtt_remote_method_calls as com
import time
import math


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be
        useful in many different programs."""

    def __init__(self):
        """Creates and stores left and right motor"""
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.color_sensor = ev3.ColorSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.MAX_SPEED = 900
        self.pixy = ev3.Sensor(driver_name="pixy-lego")
        self.mqtt_client = com.MqttClient()
        self.mqtt_client.connect_to_pc()
        self.run=True
        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected
        assert self.touch_sensor
        assert self.color_sensor
        assert self.ir_sensor
        assert self.pixy

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

    def arm_calibration(self):
        """
        Runs the arm up until the touch sensor is hit then back to the bottom again, beeping at both locations.
        Once back at in the bottom position, gripper open, set the absolute encoder position to 0.  You are calibrated!
        The Snatch3r arm needs to move 14.2 revolutions to travel from the touch sensor to the open position.
        """
        self.arm_motor.run_forever(speed_sp=self.MAX_SPEED)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop()
        ev3.Sound.beep().wait()
        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(
            position_sp=-arm_revolutions_for_full_range,
            speed_sp=self.MAX_SPEED,
            stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)

        self.arm_motor.position = 0  # Calibrate the down position as 0 (this
        # line is correct as is).

    def arm_up(self):
        """
        Moves the Snatch3r arm to the up position.
        """
        self.arm_motor.run_forever(speed_sp=self.MAX_SPEED)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop()
        ev3.Sound.beep()

    def arm_down(self):
        """
        Moves the Snatch3r arm to the down position.

        """
        # Code that attempts to do this task but has bugs.  Fix them.
        self.arm_motor.run_to_abs_pos()
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Blocks until the
        # motor
        # finishes running
        ev3.Sound.beep()

    def left_forward(self):
        """Drives the left motor forward at max speed"""
        self.left_motor.run_forever(speed_sp=self.MAX_SPEED)

    def right_forward(self):
        """Drives the right motor forward at max speed"""
        self.right_motor.run_forever(speed_sp=self.MAX_SPEED)

    def left_backward(self):
        """Drives the left motor backward at max speed"""
        self.left_motor.run_forever(speed_sp=-self.MAX_SPEED)

    def right_backward(self):
        """Drives the right motor backward at max speed"""
        self.right_motor.run_forever(speed_sp=-self.MAX_SPEED)

    def stop(self):
        """Stops both motors"""
        self.left_motor.stop()
        self.right_motor.stop()

    def shutdown(self):
        """Kill the program and say Goodbye"""
        self.kill()
        ev3.Sound.speak("Goodbye")

    def forward(self, left_speed, right_speed):
        """Moves the left motor at speed left_speed and the right motor at
            speed at right_speed"""
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def backward(self, left_speed, right_speed):
        """Moves the left motor backward at speed left_speed and the right
           motor backward at speed at right_speed"""
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def right_turn(self, left_speed, right_speed):
        """Turns the robot right by driving the right motor at right_speed
            and the left motor at negative left_speed"""
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def left_turn(self, left_speed, right_speed):
        """Turns the robot left by driving the left motor at left_speed and
            the right motor at negative right_speed"""
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def loop_forever(self):
        """Runs the program forever while self.run is True"""
        while self.run:
            pass

    def kill(self):
        """Changes self.run to False"""
        self.run=False

    def seek_beacon(self):
        """Locates the beacon and returns True when the beacon is found"""
        beacon_one = ev3.BeaconSeeker(channel=1)
        while not self.touch_sensor.is_pressed:
            # The touch sensor can be used to abort the attempt (sometimes handy during testing)

            # Done: 3. Use the beacon_seeker object to get the current heading and
            # distance.
            current_heading = beacon_one.heading  # use the beacon_seeker heading
            current_distance = beacon_one.distance  # use the beacon_seeker distance
            if current_distance == -128:
                # If the IR Remote is not found just sit idle for this program until it is moved.
                print("IR Remote not found. Distance is -128")
                self.stop()
            else:
                # Here is some code to help get you started
                if math.fabs(current_heading) < 2:
                    # Close enough of a heading to move forward
                    print("On the right heading. Distance: ", current_distance)
                    # You add more!
                    if current_distance < 2:
                        self.drive_inches(2, 300)
                        return True
                    else:
                        self.forward(500, 500)
                if math.fabs(current_heading) > 2 and math.fabs(
                        current_heading) < 10:
                    if current_heading < 0:
                        self.left_turn(200, 200)
                    else:
                        self.right_turn(200, 200)
                if math.fabs(current_heading) > 10:
                    self.stop()
                    print("Heading is too far off.")

            time.sleep(0.2)

        # The touch_sensor was pressed to abort the attempt if this code runs.
        print("Abandon ship!")
        self.stop()
        return False

    def get_color_value(self):
        """Gets the reflected light vale and sends it using the
            self.mqtt_client object"""
        color_value = self.color_sensor.reflected_light_intensity
        self.mqtt_client.send_message('get_power_up', [color_value])

    def power_up_avialable(self):
        """Moves the arm motor upwards until the touch sensor is pressed and then
        sends a message using self.mqtt_client to change_power_up_state"""
        self.arm_motor.run_forever(speed_sp=self.MAX_SPEED)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop()
        ev3.Sound.beep().wait()
        self.mqtt_client.send_message('change_power_up_state', [])
