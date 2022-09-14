class ChessWidgets:
    @staticmethod
    def basic_move_verification(table_obj, initial_square, destination_square, player_piece_color):
        xi, yi = initial_square
        xf, yf = destination_square
        initial_objc_square_list = table_obj[xi][yi]
        destination_objc_square_list = table_obj[xf][yf]
        if len(initial_objc_square_list) == 2:  # Verify if piece tried to move exists
            if initial_objc_square_list[
                1].color == player_piece_color:  # Verify if piece tried to move belong a right player
                try:  # try used to verify if destination square have 1 piece
                    if len(destination_objc_square_list) == 2:
                        if destination_objc_square_list[
                            1].color != player_piece_color:  # Verify if the destination square doest have some piece of same color
                            return True
                        else:
                            print('Já existe uma peça sua no lugar desejado')
                    else:
                        return True
                except IndexError:
                    return False
            else:
                print('a peça que deseja mover não pertence ao seu time')
        else:
            print('não existe uma peça sua na casa selecionada')

    @staticmethod
    def check_move_sintaxe(move):
        try:
            if isinstance(move, str) and (
                    7 >= int(move[0]) >= 0 and 7 >= int(move[1]) >= 0 and 7 >= int(move[2]) >= 0 and 7 >= int(
                move[3]) >= 0) and (len(move) == 4):
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def move_converter(move: str):
        if len(move) == 4:
            return (int(move[0:1]), int(move[1:2])), (int(move[2:3]), int(move[3:4]))
        else:
            return (0, 0), (0, 0)

    @staticmethod
    def square_objc_change_piece_possible(initial_position: tuple, new_position: tuple, obj_list: list) -> list:
        xi, yi = initial_position
        xf, yf = new_position
        object_list = obj_list.copy()
        if len(object_list[xf][yf]) == 2:
            object_list[xf][yf].pop(1)
        object_list[xf][yf].append(object_list[xi][yi][1])
        object_list[xi][yi].pop(1)
        object_list[xf][yf][1].update_position((xf, yf))

        return object_list

    @staticmethod
    def verify_if_after_play_self_king_its_on_check(obj_list, piece_color_move, initial_move, destination_move):
        enemy_moves = []
        king_place = ()

        obj_list = ChessWidgets.square_objc_change_piece_possible(initial_move, destination_move, obj_list)

        for x_index, row in enumerate(obj_list):

            for y_index, square in enumerate(row):
                if len(square) == 2:
                    if square[1].color != piece_color_move:
                        enemy_moves.append(square[1].possible_moves(obj_list))
                    elif square[1].color == piece_color_move:
                        if getattr(square[1], "its_king", False):
                            king_place = (x_index, y_index)

        if king_place not in enemy_moves:
            return True
        else:
            print("Seu rei está em cheque, faça algo a respeito")
            return False
