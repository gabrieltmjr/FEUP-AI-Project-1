import src.model.position as Position

class Piece:
    """This class represents a game Piece.
       var: id - piece identifier.
       var: position - represents piece position in X and Y
       var: color - represents piece color. True - blue and False - White
       var: number_value - represents piece value if game mode is Sum or King.
    """
    def __init__(self, id: int, position: Position, color: bool, number_value: int):
        self.id = id
        self.position = position
        self.color = color
        self.number_value = number_value