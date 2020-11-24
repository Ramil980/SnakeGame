import argparse
import pygame

from block import block
from graphics.drawing import message_box, redrawWindow
from snake import snake
from util.random import randomItem

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description = "Decide the Artificial Intelligence technique")
    parser.add_argument("gameMode", type=str)
    args = parser.parse_args()
    mode = args.gameMode
    print(args.gameMode)

    global dimension, rows, s, item
    dimension = 500
    rows = 20
    surface = pygame.display.set_mode((dimension, dimension))
    s = snake((60, 0, 255), (1, 15))
    item = block(randomItem(rows, s), color=(255, 0, 0))
    flag = True

    clock = pygame.time.Clock()

    if args.gameMode == "breadth-first-search":
        s.shortest.constructGraph(s.body, item.pos)
        s.shortest.configure(s)

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move(args.gameMode)
        if s.body[0].pos == item.pos:
            s.addCube()
            item = block(randomItem(rows, s), color=(255, 0, 0))
            if args.gameMode == "breadth-first-search":
                s.shortest.destroyGraph()
                s.shortest.constructGraph(s.body, item.pos)
                s.shortest.configure(s)

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print("Score: ", len(s.body))
                message_box("You Lost!", "Play again")
                s.reset((10, 10))
                break

        #break

        redrawWindow(surface, rows, dimension, s, item)

    pass

main()