import tkinter as ttk
import mqtt_remote_method_calls as com


class Single_Player(object):
    def __init__(self):
        self.turn = 'player'
        self.seq0 = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 is none, 1 is X, 2 is O
        self.seq = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.mqtt_client = com.MqttClient()
        self.mqtt_client.connect_to_ev3()
        self.root = ttk.Tk()
        self.root.title("Tic Tac Toe with Robo")
        self.main_frame = ttk.Frame(self.root, padx=10)
        self.main_frame.grid()
        self.check_var1_0 = 0
        self.check_var2_0 = 0
        self.check_var1 = 1
        self.check_var2 = 2
        self.cpu_board()

    def full_board(self):
        if sum(self.seq) <= 10:
            return True
        else:
            return

    def is_cpu_turn(self):
        if self.full_board() == True:
            if self.seq0 != self.seq:
                for k in range(len(self.seq)):
                    self.seq0[k] = self.seq[k]
                self.algorithm()
        else:
            print('Cats Game! Press New Game to Start Again')

    def cpu_turn(self):
        self.algorithm()

    def cpu_board(self):
        # Checkbox
        self.checkbox1 = ttk.Checkbutton(self.main_frame, text='X')
        self.checkbox1.grid(row=0, column=1)
        self.checkbox1['command'] = lambda: self.is_checked1()

        self.checkbox2 = ttk.Checkbutton(self.main_frame, text='O')
        self.checkbox2.grid(row=1, column=1)
        self.checkbox2['command'] = lambda: self.is_checked2()

        # Restart Button
        self.restart = ttk.Button(self.main_frame, text='New Game',
                                  command=self.reset, width=8)
        self.restart.grid(row=5, column=5)

        # TicTacToe Buttons
        self.square1 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button1)
        self.square1.grid(row=1, column=2)

        self.square2 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button2)
        self.square2.grid(row=1, column=3)

        self.square3 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button3)
        self.square3.grid(row=1, column=4)

        self.square4 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button4)
        self.square4.grid(row=2, column=2)

        self.square5 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button5)
        self.square5.grid(row=2, column=3)

        self.square6 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button6)
        self.square6.grid(row=2, column=4)

        self.square7 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button7)
        self.square7.grid(row=3, column=2)

        self.square8 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button8)
        self.square8.grid(row=3, column=3)

        self.square9 = ttk.Button(self.main_frame, text=' ', width=4,
                                  command=self.change_button9)
        self.square9.grid(row=3, column=4)

        self.root.mainloop()

    def change_button1(self):
        print('change butn')
        self.square1['text'] = self.player
        self.seq[0] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button2(self):
        self.square2['text'] = self.player
        self.seq[1] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button3(self):
        self.square3['text'] = self.player
        self.seq[2] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button4(self):
        self.square4['text'] = self.player
        self.seq[3] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button5(self):
        self.square5['text'] = self.player
        self.seq[4] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button6(self):
        self.square6['text'] = self.player
        self.seq[5] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button7(self):
        print('change butn')
        self.square7['text'] = self.player
        self.seq[6] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button8(self):
        self.square8['text'] = self.player
        self.seq[7] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button9(self):
        print('change butn')
        self.square9['text'] = self.player
        self.seq[8] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def reset(self):
        # Reset game board
        self.root.withdraw()
        self.root_err.withdraw()
        print('New Game')
        Single_Player()

    def is_checked1(self):
        if self.check_var2_0 == 1:
            self.check_error()
        else:
            self.check_var1_0 = 1
            self.player = 'X'
            self.cpu = 'O'

    def is_checked2(self):
        if self.check_var1_0 == 1:
            self.check_error()
        else:
            self.check_var2_0 = 1
            self.player = 'O'
            self.cpu = 'X'

    def check_error(self):
        self.root_err = ttk.Tk()
        self.root_err.title('ERROR: Check Console')
        self.main_frame5 = ttk.Frame(self.root_err, padx=150, pady=90)
        self.main_frame5.grid()

        self.err_bttn = ttk.Button(self.main_frame5, text='Cannot Play '
                                                          'as X and 0',
                                   width=20)
        self.err_bttn.grid(row=2, column=2)
        self.err_bttn['command'] = lambda: self.close_window()

    def open_move(self):
        print('open')
        if sum(self.seq) == 1:
            # go in center
            if self.seq[4] == 0:
                self.square5['text'] = self.cpu
                self.seq[4] = 2
                self.seq0[4] = 2
                self.turn = 'player'
                self.cpu_mark5()
            elif self.seq[4] != 0 and self.seq[0] == 0:
                self.square1['text'] = self.cpu
                self.seq[0] = 2
                self.seq0[0] = 2
                self.turn = 'player'
                self.cpu_mark1()

        elif self.seq[1] == self.seq[5] == 1 or self.seq[5] == self.seq[
            7] == 1 or \
                                self.seq[7] == self.seq[3] == 1 or self.seq[
            3] == self.seq[1] == 1:
            # prevent two options
            if self.seq[1] == self.seq[5] == 1 and self.seq[2] == 0:
                self.square3['text'] = self.cpu
                self.seq[2] = 2
                self.seq0[2] = 2
                self.turn = 'player'
                self.cpu_mark3()
            elif self.seq[5] == self.seq[7] == 1 and self.seq[8] == 0:
                self.square9['text'] = self.cpu
                self.seq[8] = 2
                self.seq0[8] = 2
                self.turn = 'player'
                self.cpu_mark9()
            elif self.seq[3] == self.seq[7] == 1 and self.seq[6] == 0:
                self.square7['text'] = self.cpu
                self.seq[6] = 2
                self.seq0[6] = 2
                self.turn = 'player'
                self.cpu_mark7()
            elif self.seq[3] == self.seq[1] == 1 and self.seq[0] == 0:
                self.square1['text'] = self.cpu
                self.seq[0] = 2
                self.seq0[0] = 2
                self.turn = 'player'
                self.cpu_mark1()
            else:
                return

    def algorithm(self):
        print('algo')
        print(self.turn)
        if self.cpu_win() == True:
            if self.turn == 'cpu':
                print('cpu win in')
                self.cpu_win()
        elif self.defense() == True:
            print(self.turn)
            if self.turn == 'cpu':
                self.defense()
        else:
            if self.turn == 'cpu':
                self.open_move()
                return
            else:
                return

    def cpu_win(self):
        print('cpu win')
        if self.turn == 'cpu':
            if self.seq[1] == self.seq[2] == 2 or self.seq[4] == self.seq[
                8] == 2 or \
                                    self.seq[3] == self.seq[6] == 2:
                if self.seq[0] == 0:
                    self.square1['text'] = self.cpu
                    self.seq[0] = 2
                    self.seq0[0] = 2
                    self.turn = 'player'
                    self.cpu_mark1()
                    return True
                else:
                    return False
            elif self.seq[0] == self.seq[1] == 2 or self.seq[5] == self.seq[
                8] == 2 or \
                                    self.seq[4] == self.seq[6] == 2:
                if self.seq[2] == 0:
                    self.square3['text'] = self.cpu
                    self.seq[2] = 2
                    self.seq0[2] = 2
                    self.turn = 'player'
                    self.cpu_mark3()
                    return True
                else:
                    return False
            elif self.seq[5] == self.seq[2] == 2 or self.seq[4] == self.seq[
                0] == 2 or \
                                    self.seq[7] == self.seq[6] == 2:
                if self.seq[8] == 0:
                    self.square9['text'] = self.cpu
                    self.seq[8] = 2
                    self.seq0[8] = 2
                    self.turn = 'player'
                    self.cpu_mark9()
                    return True
                else:
                    return False
            elif self.seq[4] == self.seq[2] == 2 or self.seq[3] == self.seq[
                0] == 2 or \
                                    self.seq[7] == self.seq[8] == 2:
                if self.seq[6] == 0:
                    self.square7['text'] = self.cpu
                    self.seq[6] = 2
                    self.seq0[6] = 2
                    self.turn = 'player'
                    self.cpu_mark7()
                    return True
                else:
                    return False
            elif self.seq[0] == self.seq[6] == 2 or self.seq[4] == self.seq[
                5] == 2:
                if self.seq[3] == 0:
                    self.square4['text'] = self.cpu
                    self.seq[3] = 2
                    self.seq0[3] = 2
                    self.turn = 'player'
                    self.cpu_mark4()
                    return True
                else:
                    return False
            elif self.seq[0] == self.seq[2] == 2 or self.seq[4] == self.seq[
                7] == 2:
                if self.seq[1] == 0:
                    self.square2['text'] = self.cpu
                    self.seq[1] = 2
                    self.seq0[1] = 2
                    self.turn = 'player'
                    self.cpu_mark2()
                    return True
                else:
                    return False
            elif self.seq[8] == self.seq[2] == 2 or self.seq[4] == self.seq[
                3] == 2:
                if self.seq[5] == 0:
                    self.square6['text'] = self.cpu
                    self.seq[5] = 2
                    self.seq0[5] = 2
                    self.turn = 'player'
                    self.cpu_mark6()
                    return True
                else:
                    return False
            elif self.seq[8] == self.seq[6] == 2 or self.seq[4] == self.seq[
                1] == 2:
                if self.seq[7] == 0:
                    self.square8['text'] = self.cpu
                    self.seq[7] = 2
                    self.seq0[7] = 2
                    self.turn = 'player'
                    self.cpu_mark8()
                    return True
                else:
                    return False
            else:
                return False

    def defense(self):
        print('defens')
        if self.seq[1] == self.seq[2] == 1 and self.seq[0] == 0 or self.seq[
            4] == self.seq[8] == 1 and self.seq[0] == 0 or \
                                        self.seq[3] == self.seq[6] == 1 and \
                                self.seq[0] == 0:
            self.square1['text'] = self.cpu
            self.seq[0] = 2
            self.seq0[0] = 2
            self.turn = 'player'
            self.cpu_mark1()
            return
        elif self.seq[0] == self.seq[1] == 1 and self.seq[2] == 0 or self.seq[
            5] == self.seq[8] == 1 and self.seq[2] == 0 or \
                                        self.seq[4] == self.seq[6] == 1 and \
                                self.seq[2] == 0:
            self.square3['text'] = self.cpu
            self.seq[2] = 2
            self.seq0[2] = 2
            self.turn = 'player'
            self.cpu_mark3()
            return
        elif self.seq[5] == self.seq[2] == 1 and self.seq[8] == 0 or self.seq[
            4] == self.seq[0] == 1 and self.seq[8] == 0 or \
                                        self.seq[7] == self.seq[6] == 1 and \
                                self.seq[8] == 0:
            self.square9['text'] = self.cpu
            self.seq[8] = 2
            self.seq0[8] = 2
            self.turn = 'player'
            self.cpu_mark9()
            return
        elif self.seq[4] == self.seq[2] == 1 and self.seq[6] == 0 or self.seq[
            3] == self.seq[0] == 1 and self.seq[6] == 0 or \
                                        self.seq[7] == self.seq[8] == 1 and \
                                self.seq[6] == 0:
            self.square7['text'] = self.cpu
            self.seq[6] = 2
            self.seq0[6] = 2
            self.turn = 'player'
            self.cpu_mark7()
            return
        elif self.seq[0] == self.seq[6] == 1 and self.seq[3] == 0 or self.seq[
            4] == self.seq[5] == 1 \
                and \
                        self.seq[3] == 0:
            self.square4['text'] = self.cpu
            self.seq[3] = 2
            self.seq0[3] = 2
            self.turn = 'player'
            self.cpu_mark4()
            return
        elif self.seq[0] == self.seq[2] == 1 and self.seq[1] == 0 or self.seq[
            4] == self.seq[7] == 1 and self.seq[1] == 0:
            self.square2['text'] = self.cpu
            self.seq[1] = 2
            self.seq0[1] = 2
            self.turn = 'player'
            self.cpu_mark2()
            return
        elif self.seq[8] == self.seq[2] == 1 and self.seq[5] == 0 or self.seq[
            4] == self.seq[3] == 1 and self.seq[5] == 0:
            self.square6['text'] = self.cpu
            self.seq[5] = 2
            self.seq0[5] = 2
            self.turn = 'player'
            self.cpu_mark6()
            return
        elif self.seq[8] == self.seq[6] == 1 and self.seq[7] == 0 or self.seq[
            4] == self.seq[1] == 1 and self.seq[7] == 0:
            self.square8['text'] = self.cpu
            self.seq[7] = 2
            self.seq0[7] = 2
            self.turn = 'player'
            self.cpu_mark8()
            return
        # corner method
        elif self.seq[0] == self.seq[8] == 1:
            if self.seq[1] == 0:
                self.square2['text'] = self.cpu
                self.seq[1] = 2
                self.seq0[1] = 2
                self.turn = 'player'
                self.cpu_mark2()
                return
            elif self.seq[3] == 0:
                self.square4['text'] = self.cpu
                self.seq[3] = 2
                self.seq0[3] = 2
                self.turn = 'player'
                self.cpu_mark4()
                return
            elif self.seq[5] == 0:
                self.square6['text'] = self.cpu
                self.seq[5] = 2
                self.seq0[5] = 2
                self.turn = 'player'
                self.cpu_mark6()
                return
            elif self.seq[7] == 0:
                self.square8['text'] = self.cpu
                self.seq[7] = 2
                self.seq0[7] = 2
                self.turn = 'player'
                self.cpu_mark8()
                return
        # corner method for other corner
        elif self.seq[2] == self.seq[6] == 1:
            if self.seq[1] == 0:
                self.square2['text'] = self.cpu
                self.seq[1] = 2
                self.seq0[1] = 2
                self.turn = 'player'
                self.cpu_mark2()
                return
            elif self.seq[3] == 0:
                self.square4['text'] = self.cpu
                self.seq[3] = 2
                self.seq0[3] = 2
                self.turn = 'player'
                self.cpu_mark4()
                return
            elif self.seq[5] == 0:
                self.square6['text'] = self.cpu
                self.seq[5] = 2
                self.seq0[5] = 2
                self.turn = 'player'
                self.cpu_mark6()
                return
            elif self.seq[7] == 0:
                self.square8['text'] = self.cpu
                self.seq[7] = 2
                self.seq0[7] = 2
                self.turn = 'player'
                self.cpu_mark8()
                return
        # block two option set-up
        elif self.seq[4] == 1 and sum(self.seq) == 4:
            if self.seq[0] == 2 and self.seq[2] == 0:
                self.square3['text'] = self.cpu
                self.seq[2] = 2
                self.seq0[2] = 2
                self.turn = 'player'
                self.cpu_mark3()
                return
            elif self.seq[2] == 2 and self.seq[0] == 0:
                self.square1['text'] = self.cpu
                self.seq[0] = 2
                self.seq0[0] = 2
                self.turn = 'player'
                self.cpu_mark1()
                return
            elif self.seq[8] == 2 and self.seq[6] == 0:
                self.square7['text'] = self.cpu
                self.seq[6] = 2
                self.seq0[6] = 2
                self.turn = 'player'
                self.cpu_mark7()
                return
            elif self.seq[6] == 2 and self.seq[8] == 0:
                self.square9['text'] = self.cpu
                self.seq[8] = 2
                self.seq0[8] = 2
                self.turn = 'player'
                self.cpu_mark9()
                return
        # almost cats game
        elif sum(self.seq) >= 7:
            print('yum')
            for k in range(len(self.seq)):
                print(self.seq[k])
                if self.seq[k] == 0:
                    if k == 0:
                        self.square1['text'] = self.cpu
                        self.cpu_mark1()
                    elif k == 1:
                        self.square2['text'] = self.cpu
                        self.cpu_mark2()
                    elif k == 2:
                        self.square3['text'] = self.cpu
                        self.cpu_mark3()
                    elif k == 3:
                        self.square4['text'] = self.cpu
                        self.cpu_mark4()
                    elif k == 4:
                        self.square5['text'] = self.cpu
                        self.cpu_mark5()
                    elif k == 5:
                        self.square6['text'] = self.cpu
                        self.cpu_mark6()
                    elif k == 6:
                        self.square7['text'] = self.cpu
                        self.cpu_mark7()
                    elif k == 7:
                        self.square8['text'] = self.cpu
                        self.cpu_mark8()
                    elif k == 8:
                        self.square9['text'] = self.cpu
                        self.cpu_mark9()
                    self.turn = self.cpu
                    return
        else:
            print('by')
            return

    def cpu_mark1(self):
        self.mqtt_client.send_message('mark_sq1', [])

    def cpu_mark2(self):
        self.mqtt_client.send_message('mark_sq2', [])

    def cpu_mark3(self):
        self.mqtt_client.send_message('mark_sq3', [])

    def cpu_mark4(self):
        self.mqtt_client.send_message('mark_sq4', [])

    def cpu_mark5(self):
        self.mqtt_client.send_message('mark_sq5', [])

    def cpu_mark6(self):
        print('done')
        self.mqtt_client.send_message('mark_sq6', [])

    def cpu_mark7(self):
        self.mqtt_client.send_message('mark_sq7', [])

    def cpu_mark8(self):
        self.mqtt_client.send_message('mark_sq8', [])

    def cpu_mark9(self):
        self.mqtt_client.send_message('mark_sq9', [])

    def close_window(self):
        self.reset()


Single_Player()
