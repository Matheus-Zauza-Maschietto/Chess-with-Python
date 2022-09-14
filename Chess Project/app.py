from chess_classes.chess_table import ChessTable

table = ChessTable()

wanna_stop = False
while not wanna_stop:
    table_objc = table.objc_table.copy()
    table.show_table(table.view_table)

    while True:
        white_move = str(input('Digite a jogada das brancas: '))
        if table.check_move_sintaxe(white_move):
            initial_square, destination_square = table.move_converter(white_move)

            if table.basic_move_verification(table_objc, initial_square, destination_square, 'white'):

                if destination_square in table.return_objc_table_list_especified(initial_square).possible_moves(
                        table_objc):

                    if destination_square in table.return_objc_table_list_especified(initial_square).possible_moves(
                            table_objc):
                        print(table_objc)
                        if table.verify_if_after_play_self_king_its_on_check(table_objc, "white", initial_square, destination_square):
                            print(table_objc)
                            table.square_objc_change_piece(initial_square, destination_square)
                            table.square_view_change_piece(initial_square, destination_square, table.return_objc_table_list_especified(destination_square))
                        break

        print('Sua jogada é invalida')

    table_objc = table.objc_table
    table.show_table(table.view_table)

    while True:
        black_move = str(input('Digite a jogada das negras: '))
        if table.check_move_sintaxe(black_move):
            initial_square, destination_square = table.move_converter(black_move)

            if table.basic_move_verification(table_objc, initial_square, destination_square, 'black'):

                if destination_square in table.return_objc_table_list_especified(initial_square).possible_moves(
                        table_objc):
                    print(table_objc)
                    if table.verify_if_after_play_self_king_its_on_check(table_objc, "black", initial_square,
                                                                         destination_square):
                        print(table_objc)
                        table.square_objc_change_piece(initial_square, destination_square)
                        table.square_view_change_piece(initial_square, destination_square,
                                                       table.return_objc_table_list_especified(destination_square))
                        break

        print('Sua jogada é invalida')

"""
casa '▓▓▓' or '   ' or '███'
Casa em branco '   ' check
peão ' ▲ ' check
cavalo ' ∑ ' check
torre ' ۩ ' check
bispo ' ᴥ '
rei ' † '
dama ' ‡ '
"""
