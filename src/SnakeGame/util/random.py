import random


def randomItem(rows, snake):
    positions = snake.body

    while True:
        #ct = 0
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

        #for pos in positions:
        #    if pos == (x, y):
        #        ct += 1
        #        break

        #if ct == 0:
        #    break

    return (x, y)
