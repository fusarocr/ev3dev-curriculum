import robot_controller as robo
import mqtt_remote_method_calls as com


def main():
    """Allows for the robot to connect to the computer and recieve commands"""
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()


main()
