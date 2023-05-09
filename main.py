import pygame, random

pygame.font.init()

def map_value(value, min1, max1, min2, max2):
    return (value - min1) / (max1 - min1) * (max2 - min2) + min2

class Graph:
    def __init__(self, screen, width, height, lines:list, range_x:int, range_y:list):
        self.screen = screen
        self.width = width
        self.height = height
        self.lines = lines
        self.range_x = range_x
        self.range_y = range_y
        self.canvas = pygame.Surface((width, height))
        self.data = {}
        for line in lines:
            self.data[line] = []
        # data = {line1: [x1, x2, x3, ...], line2: [x1, x2, x3, ...], ...}
        self.colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255)]

    def draw(self):
        self.canvas.fill((0,0,0))
        self.draw_grid()
        pygame.draw.rect(self.canvas, (255,255,255), (0,0,self.width,self.height), 1, 5)
        for idx, line in enumerate(self.lines):
            self.draw_line(line, self.colors[idx])

    def draw_line(self, line, color):
        # get the last `range_x` data points
        data = self.data[line][-self.range_x:]
        xys = []
        for idx, freq in enumerate(data):
            x = map_value(idx, 0, self.range_x, 0, self.width)
            y = map_value(freq, self.range_y[0], self.range_y[1], 0, self.height)
            # pygame.draw.circle(self.canvas, (255,255,255), (x,y), 2)
            xys.append((x,y))
        try:
            pygame.draw.lines(self.canvas, color, False, xys, 1)
        except:
            pass

    def add_data(self, line, freq):
        self.data[line].append(freq)

    def draw_grid(self):
        for x in range(0, self.width, 100):
            pygame.draw.line(self.canvas, (255,255,255), (x,0), (x,self.height), 1)
        for y in range(0, self.height, 100):
            pygame.draw.line(self.canvas, (255,255,255), (0,y), (self.width,y), 1)


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
        self.alt = Graph(self.screen, 240, 170, ["alt"], 100, [-99, 99])
        self.acc = Graph(self.screen, 240, 170, ["acc"], 100, [-99, 99])
        self.vel = Graph(self.screen, 240, 170, ["vel"], 100, [-99, 99])
        self.coor = Graph(self.screen, 860, 240, ["x", "y", "z"], 100, [-100, 100])

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
            self.screen.blit(self.coor.canvas, (280,30))


            pygame.display.flip()
            self.clock.tick(60)
            x += 1

if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


