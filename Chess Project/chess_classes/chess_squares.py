class ChessHouse:
    # OBS: A chess_piece tem que receber um objeto da peça que estará na classe, para que assim possa haver verificação
    def __init__(self, position: tuple, is_white_square: bool, initial_piece='', ):
        self.is_white_square = is_white_square
        self.content = '   '
        self.position = position
        self.chess_piece = initial_piece

    def __str__(self):
        return f'Position: {self.position}\n Content: {self.content}\n Is White: {self.is_white_square}\n'

    @property
    def is_white_square(self):
        return self._is_white_square

    @is_white_square.setter
    def is_white_square(self, value):
        if isinstance(value, bool):
            self._is_white_square = value
        self._is_white_square = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def chess_piece(self):
        return self._chess_piece

    @chess_piece.setter
    def chess_piece(self, value):
        if isinstance(value, str) and value in '‡†ᴥ۩∑▲':
            self._chess_piece = value
        else:
            self._chess_piece = ''
            raise ValueError('default value need be in one of this caracteres: "‡†ᴥ۩∑▲"')

    def recive_chess_piece(self, piece: str):
        self.chess_piece = piece
        self.content = self.content[1:2].replace(' ', self.chess_piece)

    def retrive_chess_piece(self):
        self.content = '   '
