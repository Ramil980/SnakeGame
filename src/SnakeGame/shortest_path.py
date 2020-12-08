from collections import defaultdict
from queue import Queue


class shortest_path(object):
    def __init__(self):
        self.rows = 8
        self.edges = []
        self.graph = defaultdict(list)
        self.predecessor = defaultdict(list)
        self.distance = defaultdict(list)
        self.itemPosition = (0, 0)
        self.path =[]

    def configure(self, snake):
        print(snake.head.pos, end=" ")
        print(self.itemPosition, end="\n")
        if self.checkConnectedness(snake.head.pos, self.itemPosition):
            print("\n")
            self.findShortestDistance(snake.head.pos, self.itemPosition)
            for i in range(len(self.path) - 1, 0, -1):
                snake.directionX = self.path[i - 1][0] - self.path[i][0]
                snake.directionY = self.path[i - 1][1] - self.path[i][1]
                print(snake.directionX, end=" ")
                print(snake.directionY, end=" ")
                print(self.path[i], end="\n")
                snake.turns[self.path[i]] = [snake.directionX, snake.directionY]

    def move(self, snake):
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

    # Constructs the graph
    def constructGraph(self, snakeBody, itemPosition):
        self.itemPosition = itemPosition
        for i in range(0, self.rows):
            for j in range (0, self.rows):
                if not self.isInBody(snakeBody, (i,j)):
                    if i == 0 and j == 0:
                        if (not self.isInBody(snakeBody, (i, j + 1))): self.edges.append([(i, j), (i, j+1)])
                        if (not self.isInBody(snakeBody, (i + 1, j))): self.edges.append([(i, j), (i+1, j)])
                        if (not self.isInBody(snakeBody, (self.rows - i - 1, j))): self.edges.append([(i, j), (self.rows - i - 1, j)])
                        if (not self.isInBody(snakeBody, (i, self.rows - j - 1))): self.edges.append([(i, j), (i , self.rows - j - 1)])
                    elif i == 0 and j == (self.rows - 1):
                        if (not self.isInBody(snakeBody, (i,j - 1))): self.edges.append([(i, j), (i, j - 1)])
                        if (not self.isInBody(snakeBody, (i + 1, j))): self.edges.append([(i, j), (i + 1, j)])
                        if (not self.isInBody(snakeBody, (i, j - self.rows + 1))): self.edges.append([(i, j), (i, j - self.rows + 1)])
                        if (not self.isInBody(snakeBody, (self.rows - 1, self.rows - 1))): self.edges.append([(i, j), (self.rows - 1, self.rows - 1)])
                    elif i == 0:
                        if (not self.isInBody(snakeBody, (i,j - 1))): self.edges.append([(i, j), (i, j - 1)])
                        if (not self.isInBody(snakeBody, (i,j + 1))): self.edges.append([(i, j), (i, j + 1)])
                        if (not self.isInBody(snakeBody, (i + 1, j))): self.edges.append([(i, j), (i + 1, j)])
                        if (not self.isInBody(snakeBody, (self.rows - 1, j))): self.edges.append([(i, j), (self.rows - 1, j)])
                    elif i == (self.rows - 1) and j == 0:
                        if (not self.isInBody(snakeBody, (i,j + 1))): self.edges.append([(i, j), (i, j + 1)])
                        if (not self.isInBody(snakeBody, (i - 1, j))): self.edges.append([(i, j), (i - 1, j)])
                        if (not self.isInBody(snakeBody, (i - self.rows + 1, j))): self.edges.append([(i, j), (i - self.rows + 1, j)])
                        if (not self.isInBody(snakeBody, (i, self.rows - 1))): self.edges.append([(i, j), (i, self.rows - 1)])
                    elif i == (self.rows - 1) and j == (self.rows - 1):
                        if (not self.isInBody(snakeBody, (i, j - 1))): self.edges.append([(i, j), (i, j - 1)])
                        if (not self.isInBody(snakeBody, (i - 1, j))): self.edges.append([(i, j), (i - 1, j)])
                        if (not self.isInBody(snakeBody, (0, j))): self.edges.append([(i, j), (0, j)])
                        if (not self.isInBody(snakeBody, (i, 0))): self.edges.append([(i, j), (i, 0)])
                    elif i == (self.rows - 1):
                        if (not self.isInBody(snakeBody, (i, j - 1))): self.edges.append([(i, j), (i, j - 1)])
                        if (not self.isInBody(snakeBody, (i, j + 1))): self.edges.append([(i, j), (i, j + 1)])
                        if (not self.isInBody(snakeBody, (i - 1, j))): self.edges.append([(i, j), (i - 1, j)])
                        if (not self.isInBody(snakeBody, (0, j))): self.edges.append([(i, j), (0, j)])
                    elif j == 0:
                        if (not self.isInBody(snakeBody, (i - 1, j))): self.edges.append([(i, j), (i - 1, j)])
                        if (not self.isInBody(snakeBody, (i + 1, j))): self.edges.append([(i, j), (i + 1, j)])
                        if (not self.isInBody(snakeBody, (i, j + 1))): self.edges.append([(i, j), (i, j + 1)])
                        if (not self.isInBody(snakeBody, (i, self.rows - 1))): self.edges.append([(i, j), (i, self.rows - 1)])
                    elif j == (self.rows - 1):
                        if (not self.isInBody(snakeBody, (i - 1, j))): self.edges.append([(i, j), (i - 1, j)])
                        if (not self.isInBody(snakeBody, (i + 1, j))): self.edges.append([(i, j), (i + 1, j)])
                        if (not self.isInBody(snakeBody, (i, j - 1))): self.edges.append([(i, j), (i, j - 1)])
                        if (not self.isInBody(snakeBody, (i, 0))): self.edges.append([(i, j), (i, 0)])
                    else:
                        if (not self.isInBody(snakeBody, (i - 1, j))): self.edges.append([(i, j), (i - 1, j)])
                        if (not self.isInBody(snakeBody, (i + 1, j))): self.edges.append([(i, j), (i + 1, j)])
                        if (not self.isInBody(snakeBody, (i, j + 1))): self.edges.append([(i, j), (i, j + 1)])
                        if (not self.isInBody(snakeBody, (i, j - 1))): self.edges.append([(i, j), (i, j - 1)])

        for edge in self.edges:
            a, b = edge[0], edge[1]
            self.graph[str(edge[0])].append(edge[1])

    # Destroys the graph and resets all parameters
    def destroyGraph(self):
        self.edges = []
        self.graph = defaultdict(list)
        self.predecessor = defaultdict(list)
        self.distance = defaultdict(list)
        self.itemPosition = (0, 0)
        self.path = []

    # Check whether the given position contained in snake body or not
    def isInBody(self, snakeBody, position):
        if snakeBody[0].pos == position:
            return False
        for block in snakeBody:
            if block.pos == position:
                return True
        return False

    # Check the connectnedness of source (snake's head) and destinaation (item)
    def checkConnectedness(self, source, destination):
        queue = Queue()
        visited = defaultdict(list)
        for i in range (self.rows):
            for j in range (self.rows):
                visited[str((i,j))] = False
                self.distance[str((i,j))] = 1000
                self.predecessor[str((i,j))] = -1

        visited[str(source)] = True
        self.distance[str(source)] = 0
        queue.put(source)
        while not queue.empty():
            front = queue.get()
            for i in self.graph[str(front)]:
                if visited[str(i)] == False:
                    visited[str(i)] = True
                    self.distance[str(i)] = self.distance[str(front)] + 1
                    self.predecessor[str(i)] = front
                    queue.put(i)
                    if str(i) == str(destination):
                        return True
        return False

    def findShortestDistance(self, source, destination):
        dest = destination
        self.path.append(dest)
        ct = 0
        while self.predecessor[str(dest)] != -1:
            ct += 1
            self.path.append(self.predecessor[str(dest)])
            dest = self.predecessor[str(dest)]

        for i in range(len(self.path) - 1, -1, -1):
            print(self.path[i], end=" ")
        print("\n")


