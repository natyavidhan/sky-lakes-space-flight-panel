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
    def __init__(self, screen, x, y, width, height, text):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont("Arial", 20)

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.running = True
        self.graph = Graph(self.screen, 1000, 800, ["line1", "line2", "line3", "line4", "line5", "line6"], 50, [0,100])

    def run(self):
        x = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if x%4 == 0:
                self.graph.add_data("line1", random.randint(0,100))
            if x%2 == 0:
                self.graph.add_data("line2", random.randint(0,100))
            if x%3 == 0:
                self.graph.add_data("line3", random.randint(0,100))
            if x%5 == 0:
                self.graph.add_data("line4", random.randint(0,100))
            if x%6 == 0:
                self.graph.add_data("line5", random.randint(0,100))
            if x%7 == 0:
                self.graph.add_data("line6", random.randint(0,100))
            self.graph.draw()
            self.screen.blit(self.graph.canvas, (0,0))
            pygame.display.flip()
            self.clock.tick(60)
            x += 1

if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


