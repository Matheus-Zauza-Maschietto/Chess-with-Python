class UniversalChessPiece:
    def __init__(self, color_is_white: bool, position: tuple):
        self.position = position
        if color_is_white:
            self.color = 'white'
        else:
            self.color = 'black'

    def __str__(self):
        return f'{self.color} at {self.position}'

    def update_position(self, new_position):
        self.position = (new_position[0], new_position[1])

    @staticmethod
    def move_converter(move):
        return (move[0], move[1]), (move[2], move[3])

