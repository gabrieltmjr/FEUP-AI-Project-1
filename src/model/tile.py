import src.model.position as Position

class Tile:
    """This class represents a board Tile.
       var: position - Position of the tile in the board.
       var: color - color of the tile. -1: neutral, 0: white, 1:blue
    """
    def __init__(self, position: Position, color: int):
        self.position = position
        self.color = color
