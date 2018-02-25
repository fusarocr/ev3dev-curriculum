#Run simultaneously with mover.py
from players import *
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """Creates the GUI for the program and allows for communication between
        the robot and computer"""
    root = tkinter.Tk()
    p1_canvas_power_up = tkinter.Canvas(root, width=100, height=100)
    p1_canvas_power_up.grid(row=0, column=0)
    canvas = tkinter.Canvas(root, width=400, height=400)
    canvas.grid(row=0, column=1)
    p2_canvas_power_up = tkinter.Canvas(root, width=100, height=100)
    p2_canvas_power_up.grid(row=0, column=2)

    frame = ttk.Frame(root, padding=20)
    frame.grid(row=1, column=1)
    label_player_one = ttk.Label(frame, text='Player 1')
    label_player_one.grid(row=1, column=0)
    label_player_two = ttk.Label(frame, text='Player 2')
    label_player_two.grid(row=1, column=3)
    player_one_score = ttk.Entry(frame)
    player_one_score.grid(row=2, column=0)
    player_two_score = ttk.Entry(frame)
    player_two_score.grid(row=2, column=3)

    rect1 = canvas.create_rectangle(0, 25, 25, 100, fill='blue')
    rect_power_one = p1_canvas_power_up.create_rectangle(0, 0, 100, 100,
                                                         fill='red')
    player_one = Player(rect1, canvas, 1, p1_canvas_power_up, rect_power_one,
                        player_one_score)
    root.bind('<q>', lambda event: player_one.move_up())
    root.bind('<a>', lambda event: player_one.move_down())
    root.bind('<z>', lambda event: player_one.power_up_avialable())
    root.bind('<w>', lambda event: player_one.call_for_power_up())

    rect2 = canvas.create_rectangle(375, 25, 400, 100, fill='orange')
    rect_power_two = p2_canvas_power_up.create_rectangle(0, 0, 100, 100,
                                                         fill='red')
    player_two = Player(rect2, canvas, 2, p2_canvas_power_up, rect_power_two,
                        player_two_score)
    root.bind('<p>', lambda event: player_two.move_up())
    root.bind('<l>', lambda event: player_two.move_down())

    circle = canvas.create_oval(190, 190, 210, 210, fill='black')
    ball = Ball(circle, canvas)

    start_button = ttk.Button(frame, text='Start')
    pause_button = ttk.Button(frame, text='Pause')
    reset_button = ttk.Button(frame, text='Reset')
    reset_position_button = ttk.Button(frame, text='Reset Position')
    quit_button = ttk.Button(frame, text='Quit')
    start_button.grid(row=1, column=2)
    pause_button.grid(row=2, column=2)
    reset_button.grid(row=3, column=2)
    reset_position_button.grid(row=4, column=2)
    quit_button.grid(row=5, column=2)

    mqtt_client_one = com.MqttClient(ball)
    mqtt_client_one.connect_to_mover()
    mqtt_robot_client = com.MqttClient(player_one)
    mqtt_robot_client.connect_to_ev3()
    mqtt_client_p1 = com.MqttClient(player_one)
    mqtt_client_p1.connect_to_player_one()
    mqtt_client_p2 = com.MqttClient(player_two)
    mqtt_client_p2.connect_to_player_two()

    start_button['command'] = lambda: send_coordinates(rect1, rect2, circle,
                                                       canvas,
                                                       mqtt_client_one,
                                                       player_one_score,
                                                       player_two_score)
    pause_button['command'] = lambda: mqtt_client_one.send_message("update",
                                                                   [None,
                                                                    None,
                                                                    None])
    reset_button['command'] = lambda: zero_score(player_one_score,
                                                 player_two_score)
    reset_position_button['command'] = lambda: mqtt_client_one.send_message(
        'return_to_original_position', [])
    quit_button['command'] = lambda: close(root, mqtt_client_one,
                                           mqtt_robot_client)
    root.mainloop()


def send_coordinates(rect1, rect2, circle, canvas, mqtt_client,
                     player_one_score, player_two_score):
    """Sends the current position of the two rectangles and the ball on the
    screen to the mover python file to change their locations."""
    rectangle_one_coords = canvas.coords(rect1)
    rectangle_two_cords = canvas.coords(rect2)
    circle_coords = canvas.coords(circle)
    mqtt_client.send_message("update", [rectangle_one_coords,
                                        rectangle_two_cords, circle_coords])
    zero_score(player_one_score, player_two_score)


def zero_score(player_one_score, player_two_score):
    """Zeros the score on both score boards"""
    player_one_score.delete(0, len(player_one_score.get()))
    player_two_score.delete(0, len(player_two_score.get()))
    player_one_score.insert(0, '0')
    player_two_score.insert(0, '0')


def close(root, mqtt_client_one, mqtt_robot_client):
    """Closes the entire system of programs"""
    mqtt_client_one.send_message('stop', [])
    mqtt_robot_client.send_message('kill', [])
    root.destroy()


main()
