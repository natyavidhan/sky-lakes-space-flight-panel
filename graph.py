import pygame


def map_value(value, min1, max1, min2, max2):
    return (value - min1) / (max1 - min1) * (max2 - min2) + min2

class Graph:
    def __init__(self, screen, width, height, lines:list, range_x:int, range_y:list, grid=(10, 5)):
        self.screen = screen
        self.width = width
        self.height = height
        self.lines = lines
        self.range_x = range_x
        self.range_y = range_y
        self.grid = grid
        self.canvas = pygame.Surface((width, height))
        self.label = pygame.font.SysFont("Arial", 20).render(",".join(lines), True, (255,255,255))
        self.data = {}
        for line in lines:
            self.data[line] = []
        # data = {line1: [x1, x2, x3, ...], line2: [x1, x2, x3, ...], ...}
        self.colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255)]

    def draw(self):
        self.canvas.fill((0,0,0))
        self.draw_grid()
        rect = self.label.get_rect()
        rect.center = (self.width/2, self.height/2)
        self.canvas.blit(self.label, rect)
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
        font = pygame.font.SysFont("Arial", 10)
        for x in range(self.grid[0]):
            x = map_value(x, 0, self.grid[0], 0, self.width)
            pygame.draw.line(self.canvas, (255,255,255), (x,0), (x,self.height), 1)
            # text = font.render(str(map_value(x, 0, self.width, self.range_x[0], self.range_x[1])), True, (255,255,255))
            # rect = text.get_rect()
            # rect.center = (x, self.height - 10)
            # self.canvas.blit(text, rect)
        for y in range(self.grid[1]):
            y = map_value(y, 0, self.grid[1], 0, self.height)
            pygame.draw.line(self.canvas, (255,255,255), (0,y), (self.width,y), 1)
            text = font.render(str(round(map_value(y, 0, self.height, self.range_y[0], self.range_y[1]), 3)), True, (255,255,255))
            rect = text.get_rect()
            rect.center = (10, y+rect.height/2)
            self.canvas.blit(text, rect)
