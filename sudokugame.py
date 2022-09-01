import pygame

def redrawGameWindow(win):
    win.fill((0, 0, 0))
    for number in numberList:
        number.draw_number(win)
    pygame.display.update()


class numbers():
    def __init__(self,number,pos):
        self.pos = pos
        self.number = number

    def draw_number(self,win):
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render(str(self.number), 1, (255, 0, 255))
        win.blit(text, self.pos)

    def position_number(self):
        pass

numberList =[]


def draw_board():
    pass


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("First Game")
    run = True
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
        redrawGameWindow(win)

    pygame.quit()


main()