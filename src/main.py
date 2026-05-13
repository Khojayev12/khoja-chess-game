import flet as ft
from pieces import *

#  pos_column is X coordinate
#  pos_row is Y coordinate
class BoardCell:
    def __init__(self, pos_column, pos_row, piece=None):
        self.pos_column = pos_column
        self.pos_row = pos_row
        self.piece = piece
        if ((self.pos_row+1)+(self.pos_column+1))%2 == 0:
            self.cell_bg_color = ft.Colors.TEAL_900
        else:
            self.cell_bg_color = ft.Colors.YELLOW_100

        if self.piece is not None:
            content = ft.Image(src=self.piece.get_img(), fit=ft.BoxFit.CONTAIN, width=80, height=80, margin=10)
        else:
            content = ft.Text(f"{self.pos_column}:{self.pos_row}")
        self.Container = ft.Container(width = 100, height = 100, bgcolor = self.cell_bg_color, content = content, margin=0, padding=0)

    def build(self):
        return self.Container


class PieceManager:
    def __init__(self):
        self.pawn_1_white = Pawn(0, 1, 1, "white")
        self.pawn_2_white = Pawn(1, 1, 2, "white")
        self.pawn_3_white = Pawn(2, 1, 2, "white")
        self.pawn_4_white = Pawn(3, 1, 2, "white")
        self.pawn_5_white = Pawn(4, 1, 2, "white")
        self.pawn_6_white = Pawn(5, 1, 2, "white")
        self.pawn_7_white = Pawn(6, 1, 2, "white")
        self.pawn_8_white = Pawn(7, 1, 2, "white")

        self.pawn_1_black = Pawn(0, 6, 1, "black")
        self.pawn_2_black = Pawn(1, 6, 2, "black")
        self.pawn_3_black = Pawn(2, 6, 2, "black")
        self.pawn_4_black = Pawn(3, 6, 2, "black")
        self.pawn_5_black = Pawn(4, 6, 2, "black")
        self.pawn_6_black = Pawn(5, 6, 2, "black")
        self.pawn_7_black = Pawn(6, 6, 2, "black")
        self.pawn_8_black = Pawn(7, 6, 2, "black")

    def iterate_all_figures(self):
        return [self.pawn_1_white, self.pawn_2_white, self.pawn_3_white, self.pawn_4_white, self.pawn_5_white, self.pawn_6_white, self.pawn_7_white, self.pawn_8_white, self.pawn_1_black, self.pawn_2_black, self.pawn_3_black, self.pawn_4_black, self.pawn_5_black, self.pawn_6_black, self.pawn_7_black, self.pawn_8_black]

    def check_if_piece(self, pos_column, pos_row):
        figures = self.iterate_all_figures()
        for figure in figures:
            if pos_column == figure.get_position()[0] and pos_row == figure.get_position()[1]:
                return figure
        return None


PieceManager = PieceManager()

def main(page: ft.Page):
    chess_board_rows = []
    for row in range(8):
        columns = []
        for column in range(8):
            piece = PieceManager.check_if_piece(column, row)
            columns.append(BoardCell(column, row, piece).build())
        chess_board_rows.append(ft.Row(controls=columns, spacing=0))
    #chess_board = ft.Column(controls=[ft.Row(controls=[BoardCell(r, c).build() for r in range(8)], spacing=0) for c in range(8)], spacing=0)
    chess_board = ft.Column(
        controls=chess_board_rows, spacing=0)

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                width=1000,
                height=50,
                bgcolor=ft.Colors.WHITE,
                content=chess_board,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


ft.run(main, assets_dir="assets")
