import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    # DONE: 2. Setup an mqtt_client.  Notice that since you don't need to
    # receive any messages you do NOT need to have
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Tic Tac Toe with Robo")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    # TicTacToe Buttons
    square1 = ttk.Button(main_frame, text=' ')
    square1.grid(row=1, column=1)
    square1['command']= lambda: change_square1(square1, mqtt_client)


    # # Restart Button
    # restart = ttk.Button(main_frame, text='New Game', width=8)
    # restart.grid(row=5, column=4)
    # restart['command']= lambda: reset(mqtt_client)


    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter callbacks
# ----------------------------------------------------------------------

# def reset(self):



def change_square1(square1, mqtt_client):
    mqtt_client.send_message('')
    square1['text'] = 'X'

def drive_forward(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("forward", [int(left_speed_entry.get()),
                                         int(right_speed_entry.get())])


def drive_backward(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("backward", [int(left_speed_entry.get()),
                                         int(right_speed_entry.get())])


def spin_left(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("left_turn", [int(left_speed_entry.get()),
                                         int(right_speed_entry.get())])

def spin_right(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("right_turn", [int(left_speed_entry.get()),
                                         int(right_speed_entry.get())])


def stop(mqtt_client):
    mqtt_client.send_message("stop", [])


# Arm command callbacks
def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
