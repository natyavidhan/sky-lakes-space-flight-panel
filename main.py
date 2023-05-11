import pygame, random
from graph import Graph

pygame.font.init()

def map_value(value, min1, max1, min2, max2):
    return (value - min1) / (max1 - min1) * (max2 - min2) + min2



class Button:
    def __init__(self, screen, x, y, width, height, text, action):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont("Arial", 20)
        self.action = action

    def draw(self, last_click):
        self.check_click(last_click)
        pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.width, self.height), 1)
        text = self.font.render(self.text, True, (255,255,255))
        rect = text.get_rect()
        rect.center = (self.x + self.width/2, self.y + self.height/2)
        self.screen.blit(text, rect)

    def check_click(self, last_click):
        pos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and not last_click[0]:
            self.action()

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()
        print(self.width, self.height)
        self.clock = pygame.time.Clock()
        self.running = True
        self.alt = Graph(self.screen, 240, 170, ["alt"], 100, [-99, 99], grid=(5, 5))
        self.acc = Graph(self.screen, 240, 170, ["acc"], 100, [-99, 99], grid=(5, 5))
        self.vel = Graph(self.screen, 240, 170, ["vel"], 100, [-99, 99], grid=(5, 5))
        self.coor = Graph(self.screen, 1115, 240, ["x", "y", "z"], 300, [-100, 100])

    def run(self):
        x = 0
        last = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0,0,0))
            self.alt.draw()
            self.acc.draw()
            self.vel.draw()
            self.coor.draw()
            self.alt.add_data("alt", random.randint(-25,25))
            self.acc.add_data("acc", random.randint(-25,25))
            self.vel.add_data("vel", random.randint(-25,25))
            self.coor.add_data("x", random.randint(-25,25))
            self.coor.add_data("y", random.randint(-25,10))
            self.coor.add_data("z", random.randint(-5,5))
            self.screen.blit(self.alt.canvas, (25,300))
            self.screen.blit(self.acc.canvas, (25,480))
            self.screen.blit(self.vel.canvas, (25,660))
            self.screen.blit(self.coor.canvas, (25,30))


            pygame.display.flip()
            self.clock.tick(60)
            x += 1

if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


