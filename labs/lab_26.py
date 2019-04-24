class Player:

    def __init__(self, name, token):
        self.token = token
        self.name = name


class Game:

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def move(self, x, y, player):
        self.board[x][y] = player.token

    def show_board(self):
        print(f'{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}')
        print(f'{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}')
        print(f'{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}\n')

    def check_vert(self, name, col):
        counter = 0
        column = col
        for row in self.board:
            if row[column] == name.token:
                counter += 1
                if counter == 3:
                    print(f'{name.name} wins!')
                    return True

    def check_hor(self, name):
        for row in self.board:
            if name.token in row:
                return len(set(row)) == 1

    def check_diagonal(self, name):
        diagr = (self.board[0][0], self.board[1][1], self.board[2][2])
        diagr = set(diagr)

        diagl = (self.board[0][2], self.board[1][1], self.board[2][0])
        diagl = set(diagl)

        if (name.token in diagr) or (name.token in diagl):
            if len(diagr) == 1 and diagr != ' ':
                print(f'{name.name} wins!')
                return True
            if len(diagl) == 1 and diagl != ' ':
                print(f'{name.name} wins!')
                return True


player1 = Player('Mitch', 'X')

player2 = Player('Jon', 'O')

game = Game()

game.show_board()

game.move(0, 1, player1)
game.move(1, 1, player1)
game.move(2, 1, player1)

game.show_board()

game.check_vert(player1, 0)
game.check_vert(player1, 1)
game.check_vert(player1, 2)
