import pygame

def redrawGameWindow(win,width,rows):
    win.fill((255, 255, 255))
    draw_board(width,rows,win)
    for number in numberList:
        number.draw_number(win)
    pygame.display.update()


class numbers():
    def __init__(self,number,pos):
        self.pos = pos
        self.number = number

    def draw_number(self,win):
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render(str(self.number), 1, (0, 0, 0))
        win.blit(text, self.pos)

    def position_number(self):
        pass

numberList =[]


def draw_board(win):
    pass


def draw_board(w, rows, surface):
    sizeBtwn = w // rows  # Gives us the distance between the lines

    x = 0  # Keeps track of the current x
    y = 0  # Keeps track of the current y
    for l in range(rows):  # We will draw one vertical and one horizontal line each loop
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (0,0,0), (x,0),(x,w))
        pygame.draw.line(surface, (0,0,0), (0,y),(w,y))


def main():
    pygame.init()
    height = 500
    width = 500
    rows = 9
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("First Game")
    run = True
    pos = (0, 0)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        left, middle, right = pygame.mouse.get_pressed()
        if left:
            mouse_pressed = True
            print("Left Mouse Key is being pressed")
            pos = pygame.mouse.get_pos()
            print(pos)

        keys = pygame.key.get_pressed()
        num_key = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]

        for i in range(9):
            if keys[num_key[i]]:
                number = i+1
                numberList.append(numbers(number, pos))
        redrawGameWindow(win,width,rows)
    pygame.quit()


main()