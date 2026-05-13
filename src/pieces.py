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