import tkinter as ttk

import mqtt_remote_method_calls as com


# import math
# import robot_controller as robo
# import ev3dev as ev3
# import time

class TicTacToe(object):
    def __init__(self):
        self.root = ttk.Tk()
        self.root.title('Tic Tac Toe')
        self.main_frame0 = ttk.Frame(self.root, padx=10)
        self.main_frame0.grid()

        # single / multiplayer button
        self.multiplayer = ttk.Button(self.main_frame0, text='Multi-Player')
        self.multiplayer.grid(row=0, column=0)
        self.multiplayer['command'] = lambda: self.multi()

        self.single_player = ttk.Button(self.main_frame0, text='Single Player')
        self.single_player.grid(row=1, column=0)
        self.single_player['command'] = lambda: self.single()

        self.root.mainloop()

    def single(self):
        self.root.withdraw()
        Single_Player()

    def multi(self):
        self.root.withdraw()
        Multi_Player()


class Multi_Player(object):
    def __init__(self):
        self.root = ttk.Tk()
        self.root.title('Tic Tac Toe')
        self.main_frame1 = ttk.Frame(self.root, padx=10)
        self.main_frame1.grid()
        self.normal_board = self.normal_board()

    def change_board(self):
        self.root.withdraw()
        Single_Player()

    def normal_board(self):
        # Single player button
        self.single_player = ttk.Button(self.main_frame1, text='Single Player')
        self.single_player.grid(row=0, column=0)
        self.single_player['command'] = lambda: self.change_board()

        # TicTacToe Buttons
        self.square1 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button1)
        self.square1.grid(row=1, column=1)

        self.square2 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button2)
        self.square2.grid(row=1, column=2)

        self.square3 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button3)
        self.square3.grid(row=1, column=3)

        self.square4 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button4)
        self.square4.grid(row=2, column=1)

        self.square5 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button5)
        self.square5.grid(row=2, column=2)

        self.square6 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button6)
        self.square6.grid(row=2, column=3)

        self.square7 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button7)
        self.square7.grid(row=3, column=1)

        self.square8 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button8)
        self.square8.grid(row=3, column=2)

        self.square9 = ttk.Button(self.main_frame1, text=' ', width=4,
                                  command=self.change_button9)
        self.square9.grid(row=3, column=3)

        # Restart Button
        self.restart = ttk.Button(self.main_frame1, text='New Game',
                                  command=self.reset, width=8)
        self.restart.grid(row=5, column=4)

    def reset(self):
        # Reset game board
        self.root.withdraw()
        print('New Game')
        Multi_Player()

    def check_win(self):
        # Check win
        win = self.win_game()
        if win == True:
            print('You won! Press New Game to Play Again.')

    def win_game(self):
        # How to win
        if self.square1['text'] == self.square2['text'] == self.square3[
            'text']:
            if self.square1['text'] != ' ':
                return True
        elif self.square4['text'] == self.square5['text'] == self.square6[
            'text']:
            if self.square4['text'] != ' ':
                return True
        elif self.square7['text'] == self.square8['text'] == self.square9[
            'text']:
            if self.square7['text'] != ' ':
                return True
        elif self.square1['text'] == self.square4['text'] == self.square7[
            'text']:
            if self.square1['text'] != ' ':
                return True
        elif self.square2['text'] == self.square5['text'] == self.square8[
            'text']:
            if self.square2['text'] != ' ':
                return True
        elif self.square3['text'] == self.square6['text'] == self.square9[
            'text']:
            if self.square3['text'] != ' ':
                return True
        elif self.square1['text'] == self.square5['text'] == self.square9[
            'text']:
            if self.square1['text'] != ' ':
                return True
        elif self.square3['text'] == self.square5['text'] == self.square7[
            'text']:
            if self.square3['text'] != ' ':
                return True
        else:
            print('error')

    def change_button1(self):
        """"Change the first square to X, O, or blank"""
        if self.square1['text'] == ' ':
            self.square1['text'] = 'X'
        elif self.square1['text'] == 'X':
            self.square1['text'] = 'O'
        elif self.square1['text'] == 'O':
            self.square1['text'] = ' '
        self.check_win()

    def change_button2(self):
        if self.square2['text'] == ' ':
            self.square2['text'] = 'X'
        elif self.square2['text'] == 'X':
            self.square2['text'] = 'O'
        elif self.square2['text'] == 'O':
            self.square2['text'] = ' '
        self.check_win()

    def change_button3(self):
        if self.square3['text'] == ' ':
            self.square3['text'] = 'X'
        elif self.square3['text'] == 'X':
            self.square3['text'] = 'O'
        elif self.square3['text'] == 'O':
            self.square3['text'] = ' '
        self.check_win()

    def change_button4(self):
        if self.square4['text'] == ' ':
            self.square4['text'] = 'X'
        elif self.square4['text'] == 'X':
            self.square4['text'] = 'O'
        elif self.square4['text'] == 'O':
            self.square4['text'] = ' '
        self.check_win()

    def change_button5(self):
        if self.square5['text'] == ' ':
            self.square5['text'] = 'X'
        elif self.square5['text'] == 'X':
            self.square5['text'] = 'O'
        elif self.square5['text'] == 'O':
            self.square5['text'] = ' '
        self.check_win()

    def change_button6(self):
        if self.square6['text'] == ' ':
            self.square6['text'] = 'X'
        elif self.square6['text'] == 'X':
            self.square6['text'] = 'O'
        elif self.square6['text'] == 'O':
            self.square6['text'] = ' '
        self.check_win()

    def change_button7(self):
        if self.square7['text'] == ' ':
            self.square7['text'] = 'X'
        elif self.square7['text'] == 'X':
            self.square7['text'] = 'O'
        elif self.square7['text'] == 'O':
            self.square7['text'] = ' '
        self.check_win()

    def change_button8(self):
        if self.square8['text'] == ' ':
            self.square8['text'] = 'X'
        elif self.square8['text'] == 'X':
            self.square8['text'] = 'O'
        elif self.square8['text'] == 'O':
            self.square8['text'] = ' '
        self.check_win()

    def change_button9(self):
        if self.square9['text'] == ' ':
            self.square9['text'] = 'X'
        elif self.square9['text'] == 'X':
            self.square9['text'] = 'O'
        elif self.square9['text'] == 'O':
            self.square9['text'] = ' '
        self.check_win()


class Single_Player(object):
    def __init__(self):
        self.turn = 'player'
        self.player = 'X'
        self.cpu = 'O'
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
        # self.checkers()

    # def check_win(self):
    #     # Check win
    #     win = self.win_game()
    #     if win == True:
    #         print('Press New Game to Play Again.')
    #         return True
    #     return False
    #
    # def win_game(self):
    #     # How to win
    #     if self.square1['text'] == self.square2['text'] == \
    #             self.square3[
    #                 'text']:
    #         if self.square1['text'] != ' ':
    #             return True
    #     elif self.square4['text'] == self.square5['text'] == \
    #             self.square6[
    #                 'text']:
    #         if self.square4['text'] != ' ':
    #             return True
    #     elif self.square7['text'] == self.square8['text'] == \
    #             self.square9[
    #                 'text']:
    #         if self.square7['text'] != ' ':
    #             return True
    #     elif self.square1['text'] == self.square4['text'] == \
    #             self.square7[
    #                 'text']:
    #         if self.square1['text'] != ' ':
    #             return True
    #     elif self.square2['text'] == self.square5['text'] == \
    #             self.square8[
    #                 'text']:
    #         if self.square2['text'] != ' ':
    #             return True
    #     elif self.square3['text'] == self.square6['text'] == \
    #             self.square9[
    #                 'text']:
    #         if self.square3['text'] != ' ':
    #             return True
    #     elif self.square1['text'] == self.square5['text'] == \
    #             self.square9[
    #                 'text']:
    #         if self.square1['text'] != ' ':
    #             return True
    #     elif self.square3['text'] == self.square5['text'] == \
    #             self.square7[
    #                 'text']:
    #         if self.square3['text'] != ' ':
    #             return True
    #     else:
    #         print('error')

    def full_board(self):
        # print('checking board')
        # sum = 0
        # for k in range(len(self.seq)):
        #     print(self.seq[k])
        #     if self.seq[k] == 0:
        #         sum = sum + 1
        # print('sum', sum)
        # if sum != 0:
        #     print('sum inn', sum)
        #     sum = 0
        #     return True
        # else:
        #     print('Cats Game! Press New Game to Start Again')
        if sum(self.seq) <= 10:
            print('sum,sum', sum(self.seq))
            return True
        else:
            return

    def is_cpu_turn(self):
        print('cpu tun')
        print(self.turn)
        if self.full_board() == True:
            if self.seq0 != self.seq:
                for k in range(len(self.seq)):
                    self.seq0[k] = self.seq[k]
                self.algorithm()
        else:
            print('1 Cats Game! Press New Game to Start Again')

    def cpu_turn(self):
        self.algorithm()

    def change_board(self):
        self.root.withdraw()
        Multi_Player()

    def cpu_board(self):
        # Checkbox
        self.checkbox1 = ttk.Checkbutton(self.main_frame, text='X')
        self.checkbox1.grid(row=0, column=1)
        self.checkbox1['command'] = lambda: self.is_checked(self.check_var1)

        self.checkbox2 = ttk.Checkbutton(self.main_frame, text='O')
        self.checkbox2.grid(row=1, column=1)
        self.checkbox2['command'] = lambda: self.is_checked(self.check_var2)

        # Restart Button
        self.restart = ttk.Button(self.main_frame, text='New Game',
                                  command=self.reset, width=8)
        self.restart.grid(row=5, column=5)

        # single / multiplayer button
        self.multiplayer = ttk.Button(self.main_frame, text='Multi-Player')
        self.multiplayer.grid(row=0, column=0)
        self.multiplayer['command'] = lambda: self.multi()

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

    def multi(self):
        self.root.withdraw()
        Multi_Player()

    def reset(self):
        # Reset game board
        self.root.withdraw()
        print('New Game')
        Single_Player()

    def is_checked(self, checkbox):
        print('dumbass')

    def check_error(self):
        self.root_err = ttk.Tk()
        self.root_err.title('ERROR: Check Console')
        self.main_frame5 = ttk.Frame(self.root_err, padx=150, pady=90)
        self.main_frame5.grid()

        self.err_bttn = ttk.Button(self.main_frame5, text='Cannot Play '
                                                          'as X and 0',
                                   width=20)
        self.err_bttn.grid(row=2, column=2)
        self.err_bttn['command'] = lambda: self.reset()

    def open_move(self):
        print('open')
        # go in center
        if self.seq[4] == 0:
            self.square5['text'] = self.cpu
            self.seq[4] = 2
            self.seq0[4] = 2
            self.turn = 'player'
            self.cpu_mark5()
        # #corner block
        # elif self.seq[2] == 1 and self.seq[6] == 1:
        #     if self.seq[1] == 0 and self.seq[7] == 0:
        #         self.square2['text'] = self.cpu
        #         self.seq[1] = 2
        #         self.seq0[1] = 2
        #         self.turn = 'player'
        elif self.seq[1]==self.seq[5]==1 or self.seq[5]==self.seq[7]==1 or \
                self.seq[7]==self.seq[3]==1 or self.seq[3]==self.seq[1]==1:
            # prevent two options
            if self.seq[1]==self.seq[5] and self.seq[2]==0:
                self.square3['text'] = self.cpu
                self.seq[2] = 2
                self.seq0[2] = 2
                self.turn = 'player'
                self.cpu_mark3()
            elif self.seq[5]==self.seq[7] and self.seq[8]==0:
                self.square9['text'] = self.cpu
                self.seq[8] = 2
                self.seq0[8] = 2
                self.turn = 'player'
                self.cpu_mark9()
            elif self.seq[3] == self.seq[7] and self.seq[6] == 0:
                self.square7['text'] = self.cpu
                self.seq[6] = 2
                self.seq0[6] = 2
                self.turn = 'player'
                self.cpu_mark7()
            elif self.seq[3] == self.seq[1] and self.seq[0] == 0:
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
        print(self.seq0)
        print(self.seq)
        print(self.turn)
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
        print('start pipe')
        self.mqtt_client.send_message('mark_sq1', [])

    def cpu_mark2(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq2', [])

    def cpu_mark3(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq3', [])

    def cpu_mark4(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq4', [])

    def cpu_mark5(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq5', [])

    def cpu_mark6(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq6', [])

    def cpu_mark7(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq7', [])

    def cpu_mark8(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq8', [])

    def cpu_mark9(self):
        print('start pipe')
        self.mqtt_client.send_message('mark_sq9', [])


TicTacToe()
