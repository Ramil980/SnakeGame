from collections import defaultdict


class shortest_path(object):
    def __init__(self):
        self.edges = []
        self.graph = defaultdict(list)
        self.rows = 20

    def move(self, snake):
        self.constructGraph()
        for i, c in enumerate(snake.body):
            p = c.pos[:]
            if p in snake.turns:
                turn = snake.turns[p]
                c.move(turn[0], turn[1])
                if i == len(snake.body) - 1:
                    snake.turns.pop(p)
            else:
                if c.directionX == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.directionX == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.directionY == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.directionY == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.directionX, c.directionY)

    def constructGraph(self, snakeBody):
        for i in range(0, self.rows):
            for j in range (0, self.rows):
                if not self.isInBody(snakeBody, (i,j)):
                    if i == 0 and j == 0:
                        self.edges.append([[i, j], [i, j+1]])
                        self.edges.append([[i,j], [i+1, j]])
                    elif i == 0 and j == (self.rows - 1):
                        self.edges.append([[i, j], [i, j - 1]])
                        self.edges.append([[i, j], [i + 1, j]])
                    elif i == 0:
                        self.edges.append([[i, j], [i, j - 1]])
                        self.edges.append([[i, j], [i, j + 1]])
                        self.edges.append([[i, j], [i + 1, j]])
                    elif i == (self.rows - 1) and j == 0:
                        self.edges.append([[i, j], [i, j + 1]])
                        self.edges.append([[i, j], [i - 1, j]])
                    elif i == (self.rows - 1) and j == (self.rows - 1):
                        self.edges.append([[i, j], [i, j - 1]])
                        self.edges.append([[i, j], [i - 1, j]])
                    elif i == (self.rows - 1):
                        self.edges.append([[i, j], [i, j - 1]])
                        self.edges.append([[i, j], [i, j + 1]])
                        self.edges.append([[i, j], [i - 1, j]])
                    elif j == 0:
                        self.edges.append([[i, j], [i - 1, j]])
                        self.edges.append([[i, j], [i + 1, j]])
                        self.edges.append([[i, j], [i, j + 1]])
                    elif j == (self.rows - 1):
                        self.edges.append([[i, j], [i - 1, j]])
                        self.edges.append([[i, j], [i + 1, j]])
                        self.edges.append([[i, j], [i, j - 1]])
                    else:
                        self.edges.append([[i, j], [i - 1, j]])
                        self.edges.append([[i, j], [i + 1, j]])
                        self.edges.append([[i, j], [i, j + 1]])
                        self.edges.append([[i, j], [i, j - 1]])

        for edge in self.edges:
            a, b = edge[0], edge[1]
            self.graph[str(edge[0])].append(str(edge[1]))

    def destroyGraph(self):
        pass

    def isInBody(self, snakeBody, position):
        if snakeBody[0].pos == position:
            return False
        for block in snakeBody:
            if block.pos == position:
                return True
        return False


