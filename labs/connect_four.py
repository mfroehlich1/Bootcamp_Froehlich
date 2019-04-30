class Game:

	def __init__(self):
		self.board = [
			[' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ']]

	def player_move(self, x, token):
		for row in self.board:
			if row[x] == ' ':
				row[x] = token
				break

	def show_board(self):
		for row in reversed(self.board):
			print_row = ' | '.join(row)
			print(print_row)

	def check_win(self, token, player):
		for row in self.board:
			for item in row:
				if item == token:
					if check_verticle(token):
						print(f'{player} wins!')
					if check_horizontal(token):
						print(f'{player} wins!')
					if check_down_diag(token):
						print(f'{player} wins!')
					if check_up_diag(token):
						print(f'{player} wins!')

	def check_verticle(self, token):
		pass

board = Game()

board.show_board()

print('\n')

board.player_move(1, 'X')
board.player_move(1, 'Y')
board.player_move(0, 'X')
board.player_move(1, 'Y')

board.show_board()
