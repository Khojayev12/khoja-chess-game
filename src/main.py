import flet as ft
from pieces import *

class BoardCell:
    def __init__(self, pos_x, pos_y, piece=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.piece = piece
        if ((self.pos_x+1)+(self.pos_y+1))%2 == 0:
            self.cell_bg_color = ft.Colors.TEAL_900
        else:
            self.cell_bg_color = ft.Colors.WHITE

        if self.piece is not None:
            content = ft.Image(src=f"assets/{self.piece}.png", width=80, height=80, margin=10)
        else:
            content = ft.Text(f"{self.pos_x}:{self.pos_y}")
        self.Container = ft.Container(width = 100, height = 100, bgcolor = self.cell_bg_color, content = content, margin=0, padding=0)

    def build(self):
        return self.Container


class PieceManager:
    def __init__(self):
        self.pawn_1_white = Pawn(0, 1, 1, "white")
        self.pawn_2_white = Pawn(1, 1, 2, "white")

    def check_if_piece(self, pos_x, pos_y):
        pass


def main(page: ft.Page):

    chess_board = ft.Column(controls=[ft.Row(controls=[BoardCell(r, c).build() for r in range(8)], spacing=0) for c in range(8)], spacing=0)

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


ft.run(main)
