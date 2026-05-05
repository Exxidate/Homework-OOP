import turtle

BOARD_SIZE = 8
CELL_SIZE = 60

class Piece:
    def __init__(self, color, king=False):
        self.color = color
        self.king = king

    def make_king(self):
        self.king = True


class Game:
    def __init__(self):
        self.board = [[None]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.turn = "white"
        self.selected = None
        self.possible_moves = []

        self.init_board()

    def init_board(self):
        for i in range(3):
            for j in range(BOARD_SIZE):
                if (i + j) % 2 == 1:
                    self.board[i][j] = Piece("black")

        for i in range(5, 8):
            for j in range(BOARD_SIZE):
                if (i + j) % 2 == 1:
                    self.board[i][j] = Piece("white")

    def inside(self, x, y):
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

    def get_moves(self, x, y):
        piece = self.board[y][x]
        if not piece:
            return []

        directions = []
        if piece.color == "white" or piece.king:
            directions += [(-1, -1), (1, -1)]
        if piece.color == "black" or piece.king:
            directions += [(-1, 1), (1, 1)]

        moves = []
        captures = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.inside(nx, ny):
                if self.board[ny][nx] is None:
                    moves.append((nx, ny))
                else:
                    enemy = self.board[ny][nx]
                    if enemy.color != piece.color:
                        cx, cy = nx + dx, ny + dy
                        if self.inside(cx, cy) and self.board[cy][cx] is None:
                            captures.append((cx, cy, nx, ny))

        return captures if captures else moves

    def move(self, x1, y1, x2, y2):
        piece = self.board[y1][x1]
        self.board[y1][x1] = None
        self.board[y2][x2] = piece

        if abs(x2 - x1) == 2:
            mx = (x1 + x2)//2
            my = (y1 + y2)//2
            self.board[my][mx] = None

        if piece.color == "white" and y2 == 0:
            piece.make_king()
        if piece.color == "black" and y2 == 7:
            piece.make_king()

        self.turn = "black" if self.turn == "white" else "white"

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

game = Game()

def draw_board():
    t.clear()
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            draw_cell(x, y)
            piece = game.board[y][x]
            if piece:
                draw_piece(x, y, piece)

    highlight_moves()


def draw_cell(x, y):
    screen_x = x * CELL_SIZE - 240
    screen_y = 240 - y * CELL_SIZE

    t.penup()
    t.goto(screen_x, screen_y)
    t.pendown()

    color = "white" if (x+y)%2==0 else "gray"
    t.color(color)
    t.begin_fill()

    for _ in range(4):
        t.forward(CELL_SIZE)
        t.right(90)

    t.end_fill()


def draw_piece(x, y, piece):
    screen_x = x * CELL_SIZE - 240 + CELL_SIZE//2
    screen_y = 240 - y * CELL_SIZE - CELL_SIZE//2

    t.penup()
    t.goto(screen_x, screen_y - 20)
    t.pendown()

    t.color(piece.color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    if piece.king:
        t.color("yellow")
        t.circle(10)


def highlight_moves():
    t.color("green")
    for move in game.possible_moves:
        x, y = move[0], move[1]
        screen_x = x * CELL_SIZE - 240 + CELL_SIZE//2
        screen_y = 240 - y * CELL_SIZE - CELL_SIZE//2

        t.penup()
        t.goto(screen_x, screen_y - 5)
        t.pendown()
        t.circle(5)

def click(x, y):
    board_x = int((x + 240)//CELL_SIZE)
    board_y = int((240 - y)//CELL_SIZE)

    if not game.inside(board_x, board_y):
        return

    piece = game.board[board_y][board_x]

    if piece and piece.color == game.turn:
        game.selected = (board_x, board_y)
        game.possible_moves = game.get_moves(board_x, board_y)

    elif game.selected:
        sx, sy = game.selected

        valid = False
        for move in game.possible_moves:
            if move[0] == board_x and move[1] == board_y:
                game.move(sx, sy, board_x, board_y)
                valid = True
                break

        if valid:
            game.selected = None
            game.possible_moves = []
        else:
            game.selected = None
            game.possible_moves = []

    draw_board()

screen = turtle.Screen()
screen.setup(500, 500)
screen.title("Шашки")

screen.onclick(click)

draw_board()
turtle.done()