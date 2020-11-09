import tkinter
from tkinter import messagebox

import pygame


def drawGrid(w, rows, surface):
    size = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size
        y = y + size

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface, rows, dimension, s, item):
    surface.fill((0, 0, 0))
    s.draw(surface)
    item.draw(surface)
    drawGrid(dimension, rows, surface)
    pygame.display.update()

def message_box(subject, content):
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass