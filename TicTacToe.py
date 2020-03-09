class TicTacToe:

    def __init__(self):
        self.moves = 0
        self.players = ['X', 'O']
        self.players_turn = self.players[0]
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', ''], ]
        self.is_available = [[True, True, True],
                             [True, True, True],
                             [True, True, True], ]

    def display_board(self):
        print('-------------------------------\n', end="\n")
        print("\t1\t\t2\t\t3")
        print('1\t' + self.board[0][0] + '\t|\t' + self.board[0][1] + '\t|\t' + self.board[0][2])
        print(' -------------------------')
        print('2\t' + self.board[1][0] + '\t|\t' + self.board[1][1] + '\t|\t' + self.board[1][2])
        print(' -------------------------')
        print('3\t' + self.board[2][0] + '\t|\t' + self.board[2][1] + '\t|\t' + self.board[2][2] + '\n', end="\n")

    # Confirm if move resulted in a win
    def game_status(self):

        # horizontal wins
        for index in range(3):
            if self.board[index][0] == self.board[index][1] == self.board[index][2]:
                if not (self.is_available[index][0] and self.is_available[index][1] and self.is_available[index][2]):
                    print(self.board[index][0] + " is winner")
                    self.restart()

            # vertical wins
        for index in range(3):
            if self.board[0][index] == self.board[1][index] == self.board[2][index]:
                if not (self.is_available[0][index] and self.is_available[1][index] and self.is_available[2][index]):
                    print(self.board[0][index] + " is winner")
                    self.restart()

        # diagonal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.is_available[0][0] is False:
            print(self.board[0][0] + " is winner")
            self.restart()
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.is_available[0][2] is False:
            print(self.board[0][2] + " is winner")
            self.restart()

        # Draw
        if self.moves == 8:
            print("Uh-Oh, this match was a draw!")
            self.restart()

        # confirm if move available
    def is_valid_move(self, row, column):

        if self.is_available[row][column]:
            return True
        else:
            print("\nInvalid Move!\n")
            return False

    def play(self):
        self.moves = 0
        self.players_turn = self.players[0]
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', ''], ]
        self.is_available = [[True, True, True],
                             [True, True, True],
                             [True, True, True], ]
        print("\tN E W\t\tG A M E")
        self.display_board()
        self.get_move(self.players_turn)

    def restart(self):
        restart_game = input("Game over!\nStart new game? (Y/N)\n")

        if restart_game == 'Y' or 'y':
            self.play()
        if restart_game == 'N' or 'n':
            exit(0)
        else:
            self.restart()

    def get_move(self, players_turn):
        if self.moves <= 9:
            if self.players_turn == 'X':
                print("X, your turn!")
            if self.players_turn == 'O':
                print("O, your turn!")

            row = int(input("Enter row for move: ")) - 1
            # row = self.convert_input(row)

            column = int(input("Enter Column for move: ")) - 1
            # column = self.convert_input(column)

            if self.is_valid_move(row, column):
                self.board[row][column] = players_turn
                self.moves += 1
                self.is_available[row][column] = False
                self.display_board()
                self.game_status()
                if self.players_turn == self.players[0]:
                    self.players_turn = self.players[1]
                    self.get_move(self.players_turn)
                if self.players_turn == self.players[1]:
                    self.players_turn = self.players[0]
                    self.get_move(self.players_turn)
            else:
                self.get_move(self.players_turn)
        else:
            self.restart()


"""
    def convert_input(self, user_input):
        if type(user_input) == 'int':
            if 1 <= user_input <= 3:
                return int(user_input) - 1
            else:
                print("Input must be between 1-3, try again")
                self.get_move(self.players_turn)
        else:
            print("Input must be between 1-3 , try again")
            self.get_move(self.players_turn)
            print(type(user_input))
"""
