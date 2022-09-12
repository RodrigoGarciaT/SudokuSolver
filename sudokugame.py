import pygame
import sudokuGenerator
import SudokuSolver
import time
from copy import deepcopy


def draw_board(w, rows, surface, startX, startY, rowSize):
    x = startX  # Keeps track of the current x
    y = startY  # Keeps track of the current y
    w = w // rowSize * rowSize
    for l in range(rows + 1):  # We will draw one vertical and one horizontal line each loop
        bold = 3 if not l % 3 else 1
        pygame.draw.line(surface, (0, 0, 0), (x, startY), (x, w + startY), bold)
        pygame.draw.line(surface, (0, 0, 0), (startX, y), (w + startX, y), bold)
        x = x + rowSize
        y = y + rowSize


def draw_title(surface, startX, startY, rowSize):
    fontSize = int(rowSize // 1.4)
    font = pygame.font.SysFont('comicsans', fontSize, True)
    text = font.render("Sudoku Game", 1, (0, 0, 0))
    posX = startX + 2 * rowSize
    posY = startY - 1.5 * rowSize
    surface.blit(text, (posX + rowSize / 6, posY + rowSize / 4))


def draw_sudoku(board, startX, startY, rowSize, rows):
    for i in range(0, rows):
        for j in range(0, rows):
            pos = (startX + j * rowSize, startY + i * rowSize)
            if board[i][j]:
                numberList.append(numbers(board[i][j], pos, (0, 0, 0)))


class buttons():
    def __init__(self, text):
        self.text = text
        self.posX = 9999
        self.posY = 9999
        self.sizeX = 9999
        self.sizeY = 9999

    def draw(self, surface, startX, startY, rowSize, rows):
        color = (192, 192, 192)
        spacebtw = rowSize // 2.1
        self.posX = spacebtw / 1.4 + startX
        self.posY = spacebtw + startY + rowSize * rows
        self.sizeX = rowSize * 2.5
        self.sizeY = rowSize * 1.2
        pygame.draw.rect(surface, color, pygame.Rect(self.posX, self.posY, self.sizeX, self.sizeY))

        fontSize = int(rowSize // 2.7)
        font = pygame.font.SysFont('comicsans', fontSize, True)
        text = font.render(self.text, 1, (0, 0, 0))
        surface.blit(text, (self.posX + rowSize / 6, self.posY + rowSize / 4))

    def isOver(self, surface, pos, start_board, board, startX, startY, rowSize, rows, mousepressed):
        if not mousepressed:
            return
        if self.posX <= pos[0] <= self.posX + self.sizeX:
            if self.posY <= pos[1] <= self.posY + self.sizeY:
                print("what", pos)
                self.isClicked(surface, start_board, board, startX, startY, rowSize, rows)


class new_puzzle(buttons):
    def __init__(self, text):
        super().__init__(text)

    def isClicked(self, surface, start_board, board, startX, startY, rowSize, rows):
        start_board.clear()
        board.clear()
        start_board += sudokuGenerator.generate_sudoku()
        board += deepcopy(start_board)
        numberList.clear()
        draw_sudoku(board, startX, startY, rowSize, rows)
        print(start_board)


class check_puzzle(buttons):
    def __init__(self, text):
        super().__init__(text)

    def isClicked(self, surface, start_board, board, startX, startY, rowSize, rows):
        msg = "Solved"
        for i in range(9):
            for j in range(9):
                if not SudokuSolver.check_correctness(board[i][j], i, j, board):
                    print("you failed")
                    msg = "You Failed"

        fontSize = int(rowSize)
        print(fontSize)
        font = pygame.font.SysFont('comicsans', fontSize, True)
        text = font.render(msg, 1, (255, 0, 0))

        print(text)
        surface.blit(text, (startX+2.5*rowSize, startY+ rowSize*3.5))
        pygame.display.update()
        time.sleep(2)


class solve_puzzle(buttons):
    def __init__(self, text):
        super().__init__(text)

    def isClicked(self, surface, start_board, board, startX, startY, rowSize, rows):
        copyboard = deepcopy(start_board)
        sudoku_lists = SudokuSolver.main(copyboard)
        print(len(sudoku_lists))
        for i in sudoku_lists:
            board.clear()
            numberList.clear()
            board += i
            draw_sudoku(start_board, startX, startY, rowSize, rows)
            for j in range(9):
                for k in range(9):
                    pos = (startX + k * rowSize, startY + j * rowSize)
                    if not start_board[j][k]:
                        numbers(board[j][k], pos, (0, 0, 255))
            OccupiedSpaces = {}
            for number in reversed(numberList):
                number.draw_number(surface, OccupiedSpaces, rowSize, startX, startY)
            print(board)
            pygame.display.update()
            time.sleep(5)


button1 = new_puzzle("New Puzzle")
button2 = check_puzzle("Check Puzzle")
button3 = solve_puzzle("Solve Puzzle")


class numbers():
    def __init__(self, number, pos, color):
        self.pos = pos
        self.number = number
        self.color = color

    def draw_number(self, win, OccupiedSpaces, rowSize, startX, startY):
        fontSize = int(rowSize // 1.8)
        font = pygame.font.SysFont('comicsans', fontSize, True)
        text = font.render(str(self.number), 1, self.color)
        self.position_number(rowSize, startX, startY)

        if self.pos not in OccupiedSpaces:
            if self.number:
                win.blit(text, self.pos)
        else:
            numberList.remove(self)
        OccupiedSpaces[self.pos] = True

    def position_number(self, rowSize, startX, startY):
        self.pos = ((self.pos[0] - startX) // rowSize * rowSize + (rowSize / 2) - (rowSize / 5.4) + startX,
                    (self.pos[1] - startY) // rowSize * rowSize + (rowSize / 4) + startY)


numberList = []


def redrawGameWindow(win, width, rows, startX, startY, rowSize):
    win.fill((255, 255, 255))
    draw_title(win, startX, startY, rowSize)
    draw_board(width, rows, win, startX, startY, rowSize)
    button1.draw(win, startX, startY, rowSize, rows)
    button2.draw(win, startX + rowSize * 3, startY, rowSize, rows)
    button3.draw(win, startX + rowSize * 6, startY, rowSize, rows)
    OccupiedSpaces = {}
    for number in reversed(numberList):
        number.draw_number(win, OccupiedSpaces, rowSize, startX, startY)
    OccupiedSpaces.clear()
    pygame.display.update()


def main():
    pygame.init()
    width = 500
    rows = 9
    rowSize = width // rows
    startX = 50
    startY = 100
    run = True
    pos = (0, 0)
    start_board = sudokuGenerator.generate_sudoku()
    board = deepcopy(start_board)

    for i in start_board:
        print(i)
    draw_sudoku(board, startX, startY, rowSize, rows)
    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("First Game")
    clock = pygame.time.Clock()
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        left, middle, right = pygame.mouse.get_pressed()
        if left:
            mouse_pressed = True
            print("Left Mouse Key is being pressed")
            pos = pygame.mouse.get_pos()
            print(pos)
        else:
            mouse_pressed = False
        keys = pygame.key.get_pressed()
        num_key = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                   pygame.K_8, pygame.K_9,
                   pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6,
                   pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

        for i in range(20):
            if keys[num_key[i]]:
                number = i % 10
                if startX < pos[0] < (rowSize * rows) + startX and startY < pos[1] < (rowSize * rows) + startY:

                    x = (pos[0] - startX) // rowSize
                    y = (pos[1] - startY) // rowSize
                    if not start_board[y][x]:
                        print("hello")
                        board[y][x] = number
                        numberList.append(numbers(number, pos, (0, 0, 255)))
        button1.isOver(win, pos, start_board, board, startX, startY, rowSize, rows, mouse_pressed)
        button2.isOver(win, pos, start_board, board, startX, startY, rowSize, rows, mouse_pressed)
        button3.isOver(win, pos, start_board, board, startX, startY, rowSize, rows, mouse_pressed)
        print("finishedloop")
        redrawGameWindow(win, width, rows, startX, startY, rowSize)
    pygame.quit()


main()
