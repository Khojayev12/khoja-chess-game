import flet as ft

class Pawn:
    def __init__(self, pos_column, pos_row, pawn_num, color):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.pawn_num = pawn_num
        self.color = color
        self.png_path = f"{self.color}-pawn.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_column, self.pos_row]


class Rook:
    def __init__(self, pos_column, pos_row, rook_num, color):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.rook_num = rook_num
        self.color = color
        self.png_path = f"{self.color}-rook.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_column, self.pos_row]


class Knight:
    def __init__(self, pos_column, pos_row, knight_num, color):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.knight_num = knight_num
        self.color = color
        self.png_path = f"{self.color}-knight.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_column, self.pos_row]


class Bishop:
    def __init__(self, pos_column, pos_row, bishop_num, color):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.bishop_num = bishop_num
        self.color = color
        self.png_path = f"{self.color}-bishop.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_column, self.pos_row]

class Queen:
    def __init__(self, pos_column, pos_row, color):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.color = color
        self.png_path = f"{self.color}-queen.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_column, self.pos_row]

class King:
    def __init__(self, pos_column, pos_row, color):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.color = color
        self.png_path = f"{self.color}-king.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_column, self.pos_row]