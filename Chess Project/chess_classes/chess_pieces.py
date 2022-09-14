from .chess_widgets import ChessWidgets


class UniversalChessPiece:
    def __init__(self, color_is_white: bool, position: tuple):
        self.position = position
        self.position_list = []
        if color_is_white:
            self.color = 'white'
        else:
            self.color = 'black'

    def __str__(self):
        return f'{self.color} at {self.position}'

    def update_position(self, new_position):
        self.position = (new_position[0], new_position[1])
        self.position_list.append(new_position)

    @staticmethod
    def move_converter(move):
        return (move[0], move[1]), (move[2], move[3])



class Pawn(UniversalChessPiece):
    def __init__(self, color_is_white, position, string_piece_version):
        UniversalChessPiece.__init__(self, color_is_white=color_is_white, position=position, )
        self.string_piece_version = string_piece_version

    def possible_moves(self, obj_list):
        x, y = self.position
        if self.color == 'white':
            possible_moves = [(x + 1, y)]
            if len(obj_list[x + 1][y + 1]) == 2:
                if obj_list[x + 1][y + 1][1].color == 'black':
                    possible_moves.append((x + 1, y + 1))

            if len(obj_list[x + 1][y - 1]) == 2:
                if obj_list[x + 1][y - 1][1].color == 'black':
                    possible_moves.append((x + 1, y - 1))
            if len(self.position_list) == 0:
                possible_moves.append((x + 2, y))
            return possible_moves

        elif self.color == 'black':
            possible_moves = [(x - 1, y)]
            if len(obj_list[x - 1][y + 1]) == 2:
                if obj_list[x - 1][y + 1][1].color == 'white':
                    possible_moves.append((x - 1, y + 1))
            if len(obj_list[x - 1][y - 1]) == 2:
                if obj_list[x - 1][y - 1][1].color == 'white':
                    possible_moves.append((x - 1, y - 1))
            if len(self.position_list) == 0:
                possible_moves.append((x - 2, y))
            return possible_moves
        else:
            raise ValueError


class Rook(UniversalChessPiece):
    def __init__(self, color_is_white, position, string_piece_version):
        UniversalChessPiece.__init__(self, color_is_white=color_is_white, position=position, )
        self.string_piece_version = string_piece_version

    def possible_moves(self, obj_list):
        x, y = self.position
        possible_moves = []
        if self.color == 'white' or self.color == 'black':
            for square in range(x - 1, -1, -1):
                if len(obj_list[square][y]) == 1:
                    possible_moves.append((square, y))
                elif obj_list[square][y][1].color != self.color:
                    possible_moves.append((square, y))
                    break
                else:
                    break
            for square in range(x + 1, 8):
                if len(obj_list[square][y]) == 1:
                    possible_moves.append((square, y))
                elif obj_list[square][y][1].color != self.color:
                    possible_moves.append((square, y))
                    break
                else:
                    break
            for square in range(y + 1, 8):
                if len(obj_list[x][square]) == 1:
                    possible_moves.append((x, square))
                elif obj_list[x][square][1].color != self.color:
                    possible_moves.append((x, square))
                    break
                else:
                    break
            for square in range(y - 1, -1, -1):
                if len(obj_list[x][square]) == 1:
                    possible_moves.append((x, square))
                elif obj_list[x][square][1].color != self.color:
                    possible_moves.append((x, square))
                    break
                else:
                    break
            return possible_moves
        else:
            raise ValueError


class Knight(UniversalChessPiece):
    def __init__(self, color_is_white, position, string_piece_version):
        UniversalChessPiece.__init__(self, color_is_white=color_is_white, position=position, )
        self.string_piece_version = string_piece_version

    def possible_moves(self, obj_list):
        x, y = self.position
        possible_moves = [(x + 2, y + 1), (x + 2, y - 1), (x + 1, y + 2), (x + 1, y - 2), (x - 2, y + 1),
                          (x - 2, y - 1), (x - 1, y + 2), (x - 1, y - 2)]
        for possible_move_position in possible_moves:
            if 7 >= possible_move_position[0] >= 0 and 7 >= possible_move_position[1] >= 0:
                if len(obj_list[possible_move_position[0]][possible_move_position[1]]) == 2:
                    if obj_list[possible_move_position[0]][possible_move_position[1]][1].color == self.color:
                        possible_moves.remove(possible_move_position)
            else:
                possible_moves.remove(possible_move_position)
        return possible_moves


class Bishop(UniversalChessPiece):
    def __init__(self, color_is_white, position, string_piece_version):
        UniversalChessPiece.__init__(self, color_is_white=color_is_white, position=position, )
        self.string_piece_version = string_piece_version

    def possible_moves(self, obj_list):
        x, y = self.position
        possible_moves = []

        contador = 0

        # OBS: necessario arrumar uma verificação que não de erro quando se verifi

        # Down Left x+1 y-1
        if 7 - x >= y:
            distance = y
            for square in range(distance, 0, -1):
                contador += 1
                if x + contador <= 7 and y - contador >= 0:
                    if len(obj_list[x + contador][y - contador]) == 1:
                        possible_moves.append((x + contador, y - contador))
                    elif obj_list[x + contador][y + contador][1].color != self.color:
                        possible_moves.append((x + contador, y - contador))
                        break
                    else:
                        break
        else:
            distance = x
            for square in range(distance, 7):
                contador += 1
                if x + contador <= 7 and y + contador >= 0:
                    if len(obj_list[x + contador][y - contador]) == 1:
                        possible_moves.append((x + contador, y - contador))
                    elif obj_list[x + contador][y - contador][1].color != self.color:
                        possible_moves.append((x + contador, y - contador))
                        break
                    else:
                        break
                    possible_moves.append((x + contador, y - contador))
        contador = 0

        # Down Right x+1 y+1
        if 7 - x >= 7 - y:
            distance = 7 - x
        else:
            distance = 7 - y
        for square in range(distance, 7):
            contador += 1
            if x + contador <= 7 and y + contador <= 7:
                if len(obj_list[x + contador][y + contador]) == 1:
                    possible_moves.append((x + contador, y + contador))
                elif obj_list[x + contador][y + contador][1].color != self.color:
                    possible_moves.append((x + contador, y + contador))
                    break
                else:
                    break
        contador = 0

        # Up Left x-1 y-1
        if x >= y:
            distance = x
        else:
            distance = y
        for square in range(distance, 0, -1):
            contador += 1
            if x - contador >= 0 and y - contador >= 0:
                if len(obj_list[x - contador][y - contador]) == 1:
                    possible_moves.append((x - contador, y - contador))
                elif obj_list[x - contador][y - contador][1].color != self.color:
                    possible_moves.append((x - contador, y - contador))
                    break
                else:
                    break
        contador = 0

        # Up Right x-1 y+1
        if 7-y >= x:
            distance = x
            for square in range(distance, 0, -1):
                contador += 1

                if x - contador >= 0 and y + contador <= 7:
                    if len(obj_list[x - contador][y + contador]) == 1:
                        possible_moves.append((x - contador, y + contador))
                    elif obj_list[x - contador][y + contador][1].color != self.color:
                        possible_moves.append((x - contador, y + contador))
                        break
                    else:
                        break
        else:
            distance = y
            for square in range(distance, 7):
                contador += 1
                if x - contador >= 0 and y + contador <= 7:
                    if len(obj_list[x - contador][y + contador]) == 1:
                        possible_moves.append((x - contador, y + contador))
                    elif obj_list[x - contador][y + contador][1].color != self.color:
                        possible_moves.append((x - contador, y + contador))
                        break
                    else:
                        break
        return possible_moves


class Queen(Bishop, Rook, UniversalChessPiece):
    def __init__(self, color_is_white, position, string_piece_version):
        UniversalChessPiece.__init__(self, color_is_white=color_is_white, position=position, )
        self.string_piece_version = string_piece_version

    def possible_moves(self, obj_list):
        possible_moves = Bishop.possible_moves(self, obj_list)+Rook.possible_moves(self, obj_list)
        return possible_moves


class King(UniversalChessPiece):
    def __init__(self, color_is_white, position, string_piece_version):
        UniversalChessPiece.__init__(self, color_is_white=color_is_white, position=position, )
        self.string_piece_version = string_piece_version
        self.its_king = True

    def possible_moves(self, obj_list):
        x, y = self.position
        possible_moves = []
        impossible_moves = []
        tryable_moves = [(x+1, y, ), (x-1, y, ), (x, y+1, ), (x, y-1, ), (x+1, y+1, ), (x-1, y-1, ), (x+1, y-1, ), (x-1, y+1, )]

        # check impossible movesf
        for row in obj_list:
            for square in row:
                if len(square) == 2:
                    if square[1].color != self.color and type(square[1]) != type(self):
                        impossible_moves += square[1].possible_moves(obj_list)
                    else:
                        impossible_moves.append(tuple(square[1].position))

        for move in tryable_moves:
            if move not in impossible_moves and 7 >= move[0] >= 0 and 7 >= move[1] >= 0:
                possible_moves.append(move)
        return possible_moves

