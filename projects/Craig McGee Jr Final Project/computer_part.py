import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    send_and_receive_msg = com.MqttClient()
    send_and_receive_msg.connect_to_ev3()
    root = tkinter.Tk()
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()
    inches_to_drive_entry_box = ttk.Entry(frame1, width=10)
    inches_to_drive_entry_box.grid(row=2, column=0)
    inches_to_drive_label = ttk.Label(frame1, text="Type Inches Here")
    inches_to_drive_label.grid(row=1, column=0)
    speed_to_drive_entry_box = ttk.Entry(frame1, width=10)
    speed_to_drive_entry_box.grid(row=2, column=2)
    speed_to_drive_label = ttk.Label(frame1, text="Type Speed Here")
    speed_to_drive_label.grid(row=1, column=2)
    # simon_button = ttk.Button(frame1, text="Simon Says")
    # simon_button.grid()
    # go_button = ttk.Button(frame1, text="Go")
    # go_button.grid()
    # simon_button["command"] = lambda: simon_button_pressed(entry_box,
    #                                                        send_and_receive_msg)
    # go_button["command"] = lambda: go_button_pressed(entry_box,
    #                                                  send_and_receive_msg)
    # root.mainloop()

    simon_button = ttk.Button(frame1, text='Simon says')

    # Radiobutton's. We often put them onto a sub-frame,
    # to group them visually.  The 'value' identifies which is selected.
    radio_frame = ttk.Frame(frame1, borderwidth=10, relief='groove')
    radio1 = ttk.Radiobutton(radio_frame, text='Calibrate the Arm',
                             value="calibrate_the_arm")
    radio2 = ttk.Radiobutton(radio_frame, text='Move the Arm Up',
                             value="move_arm_up")
    radio3 = ttk.Radiobutton(radio_frame, text='Move the Arm Down',
                             value="move_arm_down")
    radio4 = ttk.Radiobutton(radio_frame, text="Drive For Certain Length",
                             value="drive_inches")
    radio_frame2 = ttk.Frame(frame1, borderwidth=10, relief="groove")
    radio5 = ttk.Radiobutton(radio_frame2, text="Forward",
                             value="forward_forever")
    radio6 = ttk.Radiobutton(radio_frame2, text="Backward",
                             value="backward_forever")
    radio7 = ttk.Radiobutton(radio_frame2, text="Left",
                             value="spin_left_forever")
    radio8 = ttk.Radiobutton(radio_frame2, text="Right",
                             value="spin_right_forever")
    radio9 = ttk.Radiobutton(radio_frame2, text="Stop", value="stop")

    # This Button will show how it can interact with other widgets.
    go_button = ttk.Button(frame1, text='Go')
    go_button['command'] = lambda: go_button_pressed(send_and_receive_msg)


    # Checkbutton's and Radiobutton's can have an "observer" variable
    # that is bound to the state of the Checkbutton / Radiobutton.
    radio_observer = tkinter.StringVar()
    for radio in [radio1, radio2, radio3, radio4, radio5, radio6, radio7,
                  radio8, radio9]:
        radio['variable'] = radio_observer  # They all need the SAME observer

    # Bind callbacks using 'command' and lambda, as we have seen elsewhere.
    simon_button['command'] = lambda: simon_button_pressed(radio_observer,
                                                           send_and_receive_msg,
                                                           inches_to_drive_entry_box,
                                                           speed_to_drive_entry_box)

    for radio in [radio1, radio2, radio3, radio4, radio5, radio6, radio7,
                  radio8, radio9]:
        radio['command'] = lambda: radiobutton_changed(radio_observer)

    # Layout the widgets (here, in a row with padding between them).
    # You can see more on layout in a subsequent example.
    c = 0
    for widget in [simon_button, radio_frame, go_button]:
        widget.grid(row=0, column=c, padx=20)
        c = c + 1

    for radio in [radio1, radio2, radio3, radio4]:
        radio.grid(sticky='w')

    radio_frame2.grid(row=1, column=1)
    for radio in [radio5, radio6, radio7, radio8, radio9]:
        radio.grid(sticky="w")

    root.mainloop()


def radiobutton_changed(radiobutton_observer):
    print('The radiobutton changed to', radiobutton_observer.get())


def simon_button_pressed(radiobutton_observer, send_and_receive_msg,
                         inches_to_drive_entry_box, speed_to_drive_entry_box):
    command = radiobutton_observer.get()
    if command == "drive_inches":
        inches = inches_to_drive_entry_box.get()
        speed = speed_to_drive_entry_box.get()
        print("drive_inches", [inches, speed])
        send_and_receive_msg.send_message(command, [int(inches), int(speed)])
    elif command == "forward_forever":
        speed = speed_to_drive_entry_box.get()
        print("forward_forever", speed)
        send_and_receive_msg.send_message(command, [int(speed)])
    elif command == "backward_forever":
        speed = speed_to_drive_entry_box.get()
        print("backward_forever", speed)
        send_and_receive_msg.send_message(command, [int(speed)])
    elif command == "spin_left_forever":
        speed = speed_to_drive_entry_box.get()
        print("spin_left_forever", speed)
        send_and_receive_msg.send_message(command, [int(speed)])
    elif command == "spin_right_forever":
        speed = speed_to_drive_entry_box.get()
        print("spin_right_forever", speed)
        send_and_receive_msg.send_message(command, [int(speed)])
    elif command == "stop":
        print("stop")
        send_and_receive_msg.send_message(command)
    else:
        print("Simon says", command)
        send_and_receive_msg.send_message(command)


def go_button_pressed(send_and_receive_msg):
    send_and_receive_msg.send_message("go", )


main()
