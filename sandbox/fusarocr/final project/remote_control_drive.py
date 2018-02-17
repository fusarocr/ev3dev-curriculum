import ev3dev.ev3 as ev3
import time

import robot_controller as robo

class DataContainer(object):
    """ Helper class that might be useful to communicate
    between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")
    print("IR Remote")
    print(" - Use IR remote channel 1 to drive around")
    print(" - Use IR remote channel 2 to for the arm")
    print(" - Press the Back button on EV3 to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("I R Remote")

    ev3.Leds.all_off()  # Turn the leds off
    robot = robo.Snatch3r()
    dc = DataContainer()

    # Done: 4. Add the necessary IR handler callbacks as per the instructions
    # above.
    # Remote control channel 1 is for driving the crawler tracks around
    # (none of these functions exist yet below).
    # Remote control channel 2 is for moving the arm up and down
    # (all of these functions already exist below).
    rc1 = ev3.RemoteControl(channel=1)
    rc2 = ev3.RemoteControl(channel=2)
    rc3 = ev3.RemoteControl(channel=3)
    # For our standard shutdown button.
    btn = ev3.Button()
    btn.on_backspace = lambda state: handle_shutdown(state, dc)
    rc1.on_red_up = lambda button_state: move_left_forward(button_state,
                                                           robot)
    rc1.on_red_down = lambda button_state: move_left_backward(button_state,
                                                              robot)
    rc1.on_blue_up = lambda button_state: move_right_forward(button_state,
                                                             robot)
    rc1.on_blue_down = lambda button_state: move_right_backward(button_state,
                                                                robot)
    rc2.on_red_up = lambda button_state: handle_arm_up_button(button_state,
                                                              robot)
    rc2.on_red_down = lambda button_state: handle_arm_down_button(
        button_state, robot)
    rc2.on_blue_up = lambda button_state: handle_calibrate_button(
        button_state, robot)
    rc2.on_blue_down = lambda button_state: handle_shutdown(button_state, dc)
    rc3.on_red_up = lambda button_state: place_marker(button_state)

    robot.arm_calibration()  # Start with an arm calibration in this program.

    while dc.running:
        # Done: 5. Process the RemoteControl objects.
        btn.process()
        rc1.process()
        rc2.process()
        rc3.process()
        time.sleep(0.01)

    # Done: 2. Have everyone talk about this problem together then pick one
    # member to modify libs/robot_controller.py
    # as necessary to implement the method below as per the instructions in the
    #  opening doc string. Once the code has
    # been tested and shown to work, then have that person commit their work.
    #  All other team members need to do a
    # VCS --> Update project...
    # Once the library is implemented any team member should be able to run his
    # code as stated in todo3.
    robot.shutdown()


# ----------------------------------------------------------------------
# Event handlers
# Some event handlers have been written for you (ones for the arm).
# Movement event handlers have not been provided.
# ----------------------------------------------------------------------
# Done: 6. Implement the IR handler callbacks handlers.

# Done: 7. When your program is complete, call over a TA or instructor to sign
# your checkoff sheet and do a code review.
#
# Observations you should make, IR buttons are a fun way to control the robot.

def move_left_forward(state, robot):
    """Moves the left track forward"""
    if state:
        robot.left_forward()
    else:
        robot.stop()


def move_left_backward(state, robot):
    """Moves the left track backward"""
    if state:
        robot.left_backward()
    else:
        robot.stop()


def move_right_forward(state, robot):
    """Moves the right track forward"""
    if state:
        robot.right_forward()
    else:
        robot.stop()


def move_right_backward(state, robot):
    """Moves the right track backward"""
    if state:
        robot.right_backward()
    else:
        robot.stop()


def place_marker(button_state):
    if button_state:
        ev3.Sound.speak('For my turn I go here.').wait()


def handle_arm_up_button(button_state, robot):
    """
    Moves the arm up when the button is pressed.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
    """
    if button_state:
        robot.arm_up()



def handle_arm_down_button(button_state, robot):
    """
    Moves the arm down when the button is pressed.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
    """
    if button_state:
        robot.arm_down()


def handle_calibrate_button(button_state, robot):
    """
    Has the arm go up then down to fix the starting position.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
    """
    if button_state:
        robot.arm_calibration()


def handle_shutdown(button_state, dc):
    """
    Exit the program.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        dc.running = False

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
