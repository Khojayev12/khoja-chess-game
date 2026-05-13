class Pawn:
    def __init__(self, pos_x, pos_y, pawn_num, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pawn_num = pawn_num
        self.color = color
        self.png_path = f"assets/{self.color}-pawn.png"

    def get_img(self):
        return self.png_path
    def get_position(self):
        return [self.pos_x, self.pos_y]