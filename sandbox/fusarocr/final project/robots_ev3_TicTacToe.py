import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    """
    This code is the ev3 code that allows for MQTT communication between the
    ev3 and computer. The delegate to send messages and the MqttClientis
    created.
    """
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()  # Calls a function that has a while True: loop within
    # it to avoid letting the program end.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
