class Board:
    """This class represents a Board.
       const: num_rows - constant with quantity of rows of the board.
       const: num_cols - constant with quantity of rows of the board.
       var: tiles - Tuple with tuples inside that represent all tiles of the board.
    """
    num_rows = 5
    num_cols = 5
    def __init__(self, tiles: tuple):
        self.tiles = tiles