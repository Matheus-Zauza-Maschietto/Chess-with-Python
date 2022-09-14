from .chess_squares import ChessHouse
from .chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King
from .chess_widgets import ChessWidgets


class ChessTable(ChessWidgets):
    def __init__(self):

        self.view_table = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        self.objc_table = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        self.create_tables()
        self.add_king_piece()

        '''self.pawn = Pawn(position=(1, 3), color_is_white=True, string_piece_version='▲')
        self.objc_table[1][3].append(self.pawn)
        self.view_table[1][3] = self.white_square(chess_piece='▲', piece_color='white')
        self.white_pieces_list.append(self.pawn)

        self.pawnblack = Pawn(position=(3, 2), color_is_white=False, string_piece_version='▲')
        self.objc_table[3][2].append(self.pawnblack)
        self.view_table[3][2] = self.black_square(chess_piece='▲', piece_color='black')
        self.black_pieces_list.append(self.pawnblack)

        self.pawn2 = Pawn(position=(1, 6), color_is_white=True, string_piece_version='▲')
        self.objc_table[1][6].append(self.pawn2)
        self.view_table[1][6] = self.black_square(chess_piece='▲', piece_color='white')
        self.white_pieces_list.append(self.pawn2)

        self.rook = Rook(position=(5, 6), color_is_white=False, string_piece_version='۩')
        self.objc_table[5][6].append(self.rook)
        self.view_table[5][6] = self.black_square(chess_piece='۩', piece_color='black')
        self.black_pieces_list.append(self.rook)

        self.knight = Knight(position=(1, 1), color_is_white=True, string_piece_version='∑')
        self.objc_table[1][1].append(self.knight)
        self.view_table[1][1] = self.white_square(chess_piece='∑', piece_color='white')
        self.white_pieces_list.append(self.knight)
'''
        self.bishop = Bishop(position=(7, 3), color_is_white=False, string_piece_version='ᴥ')
        self.objc_table[7][3].append(self.bishop)
        self.view_table[7][3] = self.white_square(chess_piece='ᴥ', piece_color='black')

        self.queen = Queen(position=(5, 4), color_is_white=True, string_piece_version='‡')
        self.objc_table[5][4].append(self.queen)
        self.view_table[5][4] = self.black_square(chess_piece='‡', piece_color='white')

    def return_objc_table_list_especified(self, position: tuple):
        return self.objc_table[position[0]][position[1]][1]

    def add_king_piece(self):
        self.white_king = King(position=(0, 4), color_is_white=True, string_piece_version='†')
        self.objc_table[0][4].append(self.white_king)
        self.view_table[0][4] = self.white_square(chess_piece='†', piece_color='white')

        self.black_king = King(position=(7, 4), color_is_white=False, string_piece_version='†')
        self.objc_table[7][4].append(self.black_king)
        self.view_table[7][4] = self.black_square(chess_piece='†', piece_color='black')



    @staticmethod
    def white_square(piece_color='', chess_piece=' ', ):
        if piece_color == 'white':
            return f'\033[0;34;47m {chess_piece} \033[0m'
        elif piece_color == 'black':
            return f'\033[0;30;47m {chess_piece} \033[0m'
        else:
            return f'\033[0;33;47m {chess_piece} \033[0m'

    @staticmethod
    def black_square(piece_color='white', chess_piece=' '):
        if piece_color == 'white':
            return f'\033[0;34;42m {chess_piece} \033[0m'
        elif piece_color == 'black':
            return f'\033[0;30;42m {chess_piece} \033[0m'
        else:
            return f'\033[0;33;47m {chess_piece} \033[0m'

    def create_tables(self):
        for row in range(0, 8):
            if row % 2 == 0:  # Produce rows first square white
                for square in range(0, 4):
                    # Visual table line
                    self.view_table[row].append(self.white_square())
                    self.view_table[row].append(self.black_square())
                    # Array table line
                    self.objc_table[row].append([ChessHouse((0, 0), True, )])
                    self.objc_table[row].append([ChessHouse((0, 0), False)])

            else:  # Produce rows first square black
                for square in range(0, 4):
                    # Visual table line
                    self.view_table[row].append(self.black_square())
                    self.view_table[row].append(self.white_square())
                    # Array table line
                    self.objc_table[row].append([ChessHouse((0, 0), False)])
                    self.objc_table[row].append([ChessHouse((0, 0), True, )])

    @staticmethod
    def show_table(table_list: list):
        # Display column coords
        print('  ', end='')
        for square in range(0, 8):
            print(f' {square} ', end='')
        print()

        for row in range(0, 8):
            # Display row coords
            print(row, end=' ')

            for square in range(0, 8):
                print(table_list[row][square], end='')
            print()

    def square_objc_change_piece(self, initial_position: tuple, new_position: tuple):
        xi, yi = initial_position
        xf, yf = new_position

        if len(self.objc_table[xf][yf]) == 2:
            self.objc_table[xf][yf].pop(1)
        self.objc_table[xf][yf].append(self.objc_table[xi][yi][1])
        self.objc_table[xi][yi].pop(1)
        self.objc_table[xf][yf][1].update_position((xf, yf))

    def square_view_change_piece(self, last_position: tuple, new_position: tuple, chess_piece):
        # Need Refactory
        xi, yi = last_position
        xf, yf = new_position

        # Atualiza Last position to blank
        if xi % 2 == 0 and yi % 2 == 0 or xi % 2 == 1 and yi % 2 == 1:
            self.view_table[xi][yi] = self.white_square()
        elif xi % 2 == 0 and yi % 2 == 1 or xi % 2 == 1 and yi % 2 == 0:
            self.view_table[xi][yi] = self.black_square()

        # Atualiza New position to ocupated
        if xf % 2 == 0 and yf % 2 == 0 or xf % 2 == 1 and yf % 2 == 1:
            self.view_table[xf][yf] = self.white_square(chess_piece=chess_piece.string_piece_version,
                                                        piece_color=chess_piece.color)
        elif xf % 2 == 0 and yf % 2 == 1 or xf % 2 == 1 and yf % 2 == 0:
            self.view_table[xf][yf] = self.black_square(chess_piece=chess_piece.string_piece_version,
                                                        piece_color=chess_piece.color)
