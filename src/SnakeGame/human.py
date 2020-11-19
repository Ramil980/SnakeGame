import pygame


class human(object):
    def __init__(snakef):
        pass

    def move (snakef, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    snake.directionX = -1
                    snake.directionY = 0
                    snake.turns[snake.head.pos[:]] = [snake.directionX, snake.directionY]

                elif keys[pygame.K_RIGHT]:
                    snake.directionX = 1
                    snake.directionY = 0
                    snake.turns[snake.head.pos[:]] = [snake.directionX, snake.directionY]

                elif keys[pygame.K_UP]:
                    snake.directionX = 0
                    snake.directionY = -1
                    snake.turns[snake.head.pos[:]] = [snake.directionX, snake.directionY]

                elif keys[pygame.K_DOWN]:
                    snake.directionX = 0
                    snake.directionY = 1
                    snake.turns[snake.head.pos[:]] = [snake.directionX, snake.directionY]

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