import pygame


class numbers():
    def __init__(self,number,pos):
        self.pos = pos
        self.number = number

    def draw_number(self, win, w, rows, OccupiedSpaces):
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render(str(self.number), 1, (0, 0, 0))
        self.position_number(w,rows)

        if not self.pos in OccupiedSpaces:
            if self.number:
                win.blit(text, self.pos)
        else:
            numberList.remove(self)
        OccupiedSpaces[self.pos] = True

    def position_number(self,w,rows):
        self.pos=(self.pos[0] // (w // rows)*55+(55//2)-10, self.pos[1]//(w // rows)*55+(55//5))

numberList =[]


def draw_board(w, rows, surface):
    sizeBtwn = w // rows  # Gives us the distance between the lines

    x = 50  # Keeps track of the current x
    y = 50  # Keeps track of the current y
    startPoint=50
    for l in range(rows+1):  # We will draw one vertical and one horizontal line each loop
        bold = 3 if not l%3 else 1
        pygame.draw.line(surface, (0,0,0), (x,50),(x,w+startPoint),bold)
        pygame.draw.line(surface, (0,0,0), (50,y),(w+startPoint,y),bold)
        x = x + sizeBtwn
        y = y + sizeBtwn


def redrawGameWindow(win,width,rows):
    win.fill((255, 255, 255))
    draw_board(width, rows, win)
    OccupiedSpaces={}
    for number in reversed(numberList):
        number.draw_number(win, width, rows, OccupiedSpaces)
    OccupiedSpaces.clear()
    pygame.display.update()


def main():
    pygame.init()
    height = 500
    width = 500
    rows = 9
    win = pygame.display.set_mode((1000, 1000))
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
        num_key = [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,
                   pygame.K_KP0,pygame.K_KP1,pygame.K_KP2,pygame.K_KP3,pygame.K_KP4,pygame.K_KP5,pygame.K_KP6,pygame.K_KP7,pygame.K_KP8,pygame.K_KP9]

        for i in range(20):
            if keys[num_key[i]]:
                number = i%10
                numberList.append(numbers(number, pos))
                print((pos[0] // (width // rows))*55, ' ', (pos[1]//(width // rows))*55)
        redrawGameWindow(win, width, rows)
    pygame.quit()


main()