class Piece:
    def __init__(self, numbered, king, position, color, number_value, my_tiles):
        self.numbered = numbered
        self.king = king
        self.position = position
        self.color = color
        self.number_value = number_value
        self.my_tiles = my_tiles

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Tile:
    def __init__(self, position, color, center_tile):
        self.position = position
        self.color = color
        self.center_tile = center_tile

class Board:
    num_rows = 5
    num_cols = 5
    def __init__(self, tiles):
        self.tiles = tiles

    
