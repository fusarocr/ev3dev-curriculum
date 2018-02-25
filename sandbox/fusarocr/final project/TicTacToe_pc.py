import tkinter as ttk
import mqtt_remote_method_calls as com


class SinglePlayer(object):
    """
    Class for the tic tac toe board. A Single_Player class sets up a
    tic tac toe board using a tkinter GUI.
    """

    def __init__(self):
        """ Initializes the instance variables for the SinglePlayer class
        that will be used for other methods."""
        # Place-holder Arrays for the tic tac toe board
        self.seq0 = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 is none, 1 is X, 2 is O
        self.seq = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # MQTT communication set-up
        self.mqtt_client = com.MqttClient()
        self.mqtt_client.connect_to_ev3()
        # GUI set-up
        self.root = ttk.Tk()
        self.root.title("Tic Tac Toe with Robo")
        # Create the main tkinter frame
        self.main_frame = ttk.Frame(self.root, padx=10)
        self.main_frame.grid()
        # Checkbox variables
        self.check_var1_0 = 0
        self.check_var2_0 = 0
        self.check_var1 = 1
        self.check_var2 = 2
        # Set-up the board and start the game
        self.cpu_board()

    def cpu_board(self):
        """
        Creates a tic tac toe board using tkinter. The tkinter has two
        checkboxes and a restart button
        """
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

    def is_checked1(self):
        """
        If only the 'X' checkbox is checked, changes the self.player
        instance, players mark, to 'X' and the self.cpu instance, cpu mark,
        to 'O'. Otherwise, this method then calls self.check_error
        """
        if self.check_var2_0 == 1:
            self.check_error()
        else:
            self.check_var1_0 = 1
            self.player = 'X'
            self.cpu = 'O'

    def is_checked2(self):
        """
        If only the 'O' checkbox is checked, changes the self.player
        instance, players mark, to 'X' and the self.cpu instance, cpu mark,
        to 'O'. Otherwise, this method then calls self.check_error
        """
        if self.check_var1_0 == 1:
            self.check_error()
        else:
            self.check_var2_0 = 1
            self.player = 'O'
            self.cpu = 'X'

    def check_error(self):
        """
        Creates a tkinter frame with a button that reads 'ERROR: Check
        Console'. When the button is pressed, calls self.close_window method
        """
        self.root_err = ttk.Tk()
        self.root_err.title('ERROR: Check Console')
        self.main_frame5 = ttk.Frame(self.root_err, padx=150, pady=90)
        self.main_frame5.grid()

        self.err_bttn = ttk.Button(self.main_frame5, text='Cannot Play '
                                                          'as X and 0',
                                   width=20)
        self.err_bttn.grid(row=2, column=2)
        self.err_bttn['command'] = lambda: self.close_window()

    def close_window(self):
        """ Closes the current window and calls self.reset """
        self.root_err.withdraw()
        self.reset()

    def reset(self):
        """
        Resets the tkinter by creating a blank game-board,
        while withdrawing the current tkinter tic tac toe board.
        """
        self.root.withdraw()
        print('New Game')
        SinglePlayer()

    def change_button1(self):
        """ Changes the text of square one to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square1['text'] = self.player
        self.seq[0] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button2(self):
        """ Changes the text of square two to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square2['text'] = self.player
        self.seq[1] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button3(self):
        """ Changes the text of square three to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square3['text'] = self.player
        self.seq[2] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button4(self):
        """ Changes the text of square four to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square4['text'] = self.player
        self.seq[3] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button5(self):
        """ Changes the text of square five to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square5['text'] = self.player
        self.seq[4] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button6(self):
        """ Changes the text of square six to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square6['text'] = self.player
        self.seq[5] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button7(self):
        """ Changes the text of square seven to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square7['text'] = self.player
        self.seq[6] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button8(self):
        """ Changes the text of square eight to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square8['text'] = self.player
        self.seq[7] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def change_button9(self):
        """ Changes the text of square nine to the player's mark, either 'X'
        or 'O'. The self.turn instance, which indicates which player's turn it
        is, is changed to 'cpu', while the self.is_cpu_turn method is
        called."""
        self.square9['text'] = self.player
        self.seq[8] = 1
        self.turn = 'cpu'
        self.is_cpu_turn()

    def full_board(self):
        """ Checks to see if the board is full."""
        if sum(self.seq) <= 10:
            return True
        else:
            return False

    def is_cpu_turn(self):
        """
        If the board is open and it is the computer's turn,
        the self.algorithm method will be called so the cpu can make its
        move. Otherwise, there is a cats game so print
        'Cats Game! Press New Game to Start Again'.
        """
        if self.full_board():
            if self.seq0 != self.seq:
                for k in range(len(self.seq)):
                    self.seq0[k] = self.seq[k]
                self.algorithm()
        else:
            print('Cats Game! Press New Game to Start Again')

    def algorithm(self):
        """ Determines if the computer should make a winning, defensive,
        or open move."""
        if self.cpu_win():
            if self.turn == 'cpu':
                self.cpu_win()
        elif self.defense():
            print(self.turn)
            if self.turn == 'cpu':
                self.defense()
        else:
            if self.turn == 'cpu':
                self.open_move()
            else:
                return

    def cpu_win(self):
        """
        Scans the board to see if a winning move is available for the
        computer and return True. Otherwise returns False.
        """
        if self.turn == 'cpu':
            if self.seq[1] == self.seq[2] == 2 and self.seq[0] == 0 \
                    or self.seq[4] == self.seq[8] == 2 and self.seq[0] == 0 \
                    or self.seq[3] == self.seq[6] == 2 and self.seq[0] == 0:
                self.cpu_change_square1()
                print('I win!')
                return True
            elif self.seq[0] == self.seq[1] == 2 and self.seq[2] == 0 \
                    or self.seq[5] == self.seq[8] == 2 and self.seq[2] == 0 \
                    or self.seq[4] == self.seq[6] == 2 and self.seq[2] == 0:
                self.cpu_change_square3()
                print('I win!')
                return True
            elif self.seq[5] == self.seq[2] == 2 and self.seq[8] == 0 \
                    or self.seq[4] == self.seq[0] == 2 and self.seq[8] == 0 \
                    or self.seq[7] == self.seq[6] == 2 and self.seq[8] == 0:
                self.cpu_change_square9()
                print('I win!')
                return True
            elif self.seq[4] == self.seq[2] == 2 and self.seq[6] == 0 \
                    or self.seq[3] == self.seq[0] == 2 and self.seq[6] == 0 \
                    or self.seq[7] == self.seq[8] == 2 and self.seq[6] == 0:
                self.cpu_change_square7()
                print('I win!')
                return True
            elif self.seq[0] == self.seq[6] == 2 and self.seq[3] == 0 \
                    or self.seq[4] == self.seq[5] == 2 and self.seq[3] == 0:
                self.cpu_change_square4()
                print('I win!')
                return True
            elif self.seq[0] == self.seq[2] == 2 and self.seq[1] == 0 \
                    or self.seq[4] == self.seq[7] == 2 and self.seq[1] == 0:
                self.cpu_change_square2()
                print('I win!')
                return True
            elif self.seq[8] == self.seq[2] == 2 and self.seq[5] == 0 \
                    or self.seq[4] == self.seq[3] == 2 and self.seq[5] == 0:
                self.cpu_change_square6()
                print('I win!')
                return True
            elif self.seq[8] == self.seq[6] == 2 and self.seq[7] == 0 \
                    or self.seq[4] == self.seq[1] == 2 and self.seq[7] == 0:
                self.cpu_change_square8()
                print('I win!')
                return True
            else:
                return False
        else:
            return False

    def defense(self):
        """
        Blocks the the opponent if they are about to win,
        or blocks the opponent from making a move to give them an advantage.
        """
        if self.seq[1] == self.seq[2] == 1 and self.seq[0] == 0 \
                or self.seq[4] == self.seq[8] == 1 and self.seq[0] == 0 \
                or self.seq[3] == self.seq[6] == 1 and self.seq[0] == 0:
            self.cpu_change_square1()
        elif self.seq[0] == self.seq[1] == 1 and self.seq[2] == 0 \
                or self.seq[5] == self.seq[8] == 1 and self.seq[2] == 0 \
                or self.seq[4] == self.seq[6] == 1 and self.seq[2] == 0:
            self.cpu_change_square3()
        elif self.seq[5] == self.seq[2] == 1 and self.seq[8] == 0 \
                or self.seq[4] == self.seq[0] == 1 and self.seq[8] == 0 \
                or self.seq[7] == self.seq[6] == 1 and self.seq[8] == 0:
            self.cpu_change_square9()
        elif self.seq[4] == self.seq[2] == 1 and self.seq[6] == 0 \
                or self.seq[3] == self.seq[0] == 1 and self.seq[6] == 0 \
                or self.seq[7] == self.seq[8] == 1 and self.seq[6] == 0:
            self.cpu_change_square7()
        elif self.seq[0] == self.seq[6] == 1 and self.seq[3] == 0 \
                or self.seq[4] == self.seq[5] == 1 and self.seq[3] == 0:
            self.cpu_change_square4()
        elif self.seq[0] == self.seq[2] == 1 and self.seq[1] == 0 \
                or self.seq[4] == self.seq[7] == 1 and self.seq[1] == 0:
            self.cpu_change_square2()
        elif self.seq[8] == self.seq[2] == 1 and self.seq[5] == 0 \
                or self.seq[4] == self.seq[3] == 1 and self.seq[5] == 0:
            self.cpu_change_square6()
        elif self.seq[8] == self.seq[6] == 1 and self.seq[7] == 0 \
                or self.seq[4] == self.seq[1] == 1 and self.seq[7] == 0:
            self.cpu_change_square8()
        else:
            self.stop_adavantage()

    def stop_adavantage(self):
        """ Blocks the opponent from gaining any advantage."""
        if self.seq[0] == self.seq[8] == 1:
            self.corner_method()
        elif self.seq[2] == self.seq[6] == 1:
            self.corner_method()
        elif self.seq[1] == self.seq[5] == 1 \
                or self.seq[5] == self.seq[7] == 1 \
                or self.seq[7] == self.seq[3] == 1 \
                or self.seq[3] == self.seq[1] == 1:
            self.prevent_two_paths()
        else:
            return

    def corner_method(self):
        """ If the opponent has two opposite corners, cpu makes a move to
        defend."""
        if self.seq[1] == 0:
            self.cpu_change_square2()
        elif self.seq[3] == 0:
            self.cpu_change_square4()
        elif self.seq[5] == 0:
            self.cpu_change_square6()
        elif self.seq[7] == 0:
            self.cpu_change_square8()

    def prevent_two_paths(self):
        """ Prevent the opponent from having two options to win."""
        if self.seq[1] == self.seq[5] == 1 and self.seq[2] == 0:
            self.cpu_change_square3()
        elif self.seq[5] == self.seq[7] == 1 and self.seq[8] == 0:
            self.cpu_change_square9()
        elif self.seq[3] == self.seq[7] == 1 and self.seq[6] == 0:
            self.cpu_change_square7()
        elif self.seq[3] == self.seq[1] == 1 and self.seq[0] == 0:
            self.cpu_change_square1()

    def open_move(self):
        """ Choose the best available open move."""
        if sum(self.seq) == 1:
            self.center()
        elif self.seq[4] == 2 and sum(self.seq) == 4:
            self.get_advantage()
        elif sum(self.seq) >= 7:
            self.almost_cats_game()
        else:
            return

    def center(self):
        """ Go in the center of the tic tac toe board."""
        if self.seq[4] == 0:
            self.cpu_change_square5()
        elif self.seq[4] != 0 and self.seq[0] == 0:
            self.cpu_change_square1()

    def get_advantage(self):
        """ Gain an advantage to win."""
        if self.seq[0] == 1 and self.seq[8] != 1:
            if self.seq[7] == 1:
                self.cpu_change_square7()
            elif self.seq[5] == 1:
                self.cpu_change_square3()
        elif self.seq[2] == 1 and self.seq[6] != 1:
            if self.seq[3] == 1:
                self.cpu_change_square1()
            elif self.seq[7] == 1:
                self.cpu_change_square9()
        elif self.seq[6] == 1 and self.seq[2] != 1:
            if self.seq[1] == 1:
                self.cpu_change_square1()
            elif self.seq[5] == 1:
                self.cpu_change_square9()
        elif self.seq[8] == 1 and self.seq[0] != 1:
            if self.seq[1] == 1:
                self.cpu_change_square3()
            elif self.seq[3] == 1:
                self.cpu_change_square7()

    def almost_cats_game(self):
        """ If there is goinig to be a CATS game, the cpu will make the
        first move that is available"""
        for k in range(len(self.seq)):
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

    def cpu_change_square1(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square1['text'] = self.cpu
        self.seq[0] = 2
        self.seq0[0] = 2
        self.turn = 'player'
        self.cpu_mark1()

    def cpu_change_square2(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square2['text'] = self.cpu
        self.seq[1] = 2
        self.seq0[1] = 2
        self.turn = 'player'
        self.cpu_mark2()

    def cpu_change_square3(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square3['text'] = self.cpu
        self.seq[2] = 2
        self.seq0[2] = 2
        self.turn = 'player'
        self.cpu_mark3()

    def cpu_change_square4(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square4['text'] = self.cpu
        self.seq[3] = 2
        self.seq0[3] = 2
        self.turn = 'player'
        self.cpu_mark4()

    def cpu_change_square5(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square5['text'] = self.cpu
        self.seq[4] = 2
        self.seq0[4] = 2
        self.turn = 'player'
        self.cpu_mark5()

    def cpu_change_square6(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square6['text'] = self.cpu
        self.seq[5] = 2
        self.seq0[5] = 2
        self.turn = 'player'
        self.cpu_mark6()

    def cpu_change_square7(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square7['text'] = self.cpu
        self.seq[6] = 2
        self.seq0[6] = 2
        self.turn = 'player'
        self.cpu_mark7()

    def cpu_change_square8(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square8['text'] = self.cpu
        self.seq[7] = 2
        self.seq0[7] = 2
        self.turn = 'player'
        self.cpu_mark8()

    def cpu_change_square9(self):
        """ Change the blank square to the cpu's mark and self.turn to
        'player' to indicate the player's turn."""
        self.square9['text'] = self.cpu
        self.seq[8] = 2
        self.seq0[8] = 2
        self.turn = 'player'
        self.cpu_mark9()

    def cpu_mark1(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 1"""
        self.mqtt_client.send_message('mark_sq1', [])

    def cpu_mark2(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 2"""
        self.mqtt_client.send_message('mark_sq2', [])

    def cpu_mark3(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 3"""
        self.mqtt_client.send_message('mark_sq3', [])

    def cpu_mark4(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 4"""
        self.mqtt_client.send_message('mark_sq4', [])

    def cpu_mark5(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 5"""
        self.mqtt_client.send_message('mark_sq5', [])

    def cpu_mark6(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 6"""
        self.mqtt_client.send_message('mark_sq6', [])

    def cpu_mark7(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 7"""
        self.mqtt_client.send_message('mark_sq7', [])

    def cpu_mark8(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 8"""
        self.mqtt_client.send_message('mark_sq8', [])

    def cpu_mark9(self):
        """ Sends a message to the Snatch3r robot via the MQTT client.
        Tells the robot to move to square 9"""
        self.mqtt_client.send_message('mark_sq9', [])


SinglePlayer()
