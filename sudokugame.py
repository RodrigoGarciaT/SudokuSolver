import pygame


def draw_board(w, rows, surface,startX,startY,rowSize):
    x = startX  # Keeps track of the current x
    y = startY  # Keeps track of the current y
    for l in range(rows+1):  # We will draw one vertical and one horizontal line each loop
        bold = 3 if not l%3 else 1
        pygame.draw.line(surface, (0,0,0), (x,startY),(x,w+startY),bold)
        pygame.draw.line(surface, (0,0,0), (startX,y),(w+startX,y),bold)
        x = x + rowSize
        y = y + rowSize


class numbers():
    def __init__(self,number,pos):
        self.pos = pos
        self.number = number

    def draw_number(self, win, OccupiedSpaces, rowSize,startX,startY):
        fontSize=int(rowSize//1.8)
        print(fontSize)
        font = pygame.font.SysFont('comicsans',fontSize , True)
        text = font.render(str(self.number), 1, (0, 0, 0))
        self.position_number(rowSize,startX,startY)

        if not self.pos in OccupiedSpaces:
            if self.number:
                win.blit(text, self.pos)
        else:
            numberList.remove(self)
        OccupiedSpaces[self.pos] = True

    def position_number(self, rowSize,startX,startY):
        self.pos=((self.pos[0]-startX)// rowSize*rowSize+(rowSize/2)-(rowSize/5.4)+startX, (self.pos[1]-startY)//rowSize*rowSize+(rowSize/4)+startY)

numberList =[]


def redrawGameWindow(win,width,rows, startX, startY, rowSize):
    win.fill((255, 255, 255))
    draw_board(width, rows, win, startX, startY,rowSize)
    OccupiedSpaces={}
    for number in reversed(numberList):
        number.draw_number(win, OccupiedSpaces,rowSize,startX,startY)
    OccupiedSpaces.clear()
    pygame.display.update()


def main():
    pygame.init()
    width = 450
    rows = 9
    rowSize=width//rows
    startX=15
    startY=15
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
                print(pos[0] // rowSize*rowSize, ' ', (pos[1]//rowSize)*rowSize)
        redrawGameWindow(win, width, rows,startX,startY,rowSize)
    pygame.quit()


main()