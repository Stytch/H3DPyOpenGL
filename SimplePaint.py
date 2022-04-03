import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *
pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_point(my_points):
    glBegin(GL_POINTS)
    for p in my_points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px)*math.cos(2*math.pi*px)
        glVertex2f(px, py)
    glEnd()


def plot_lines(my_lines):
    for my_points in my_lines:
        glBegin(GL_LINE_STRIP)
        for p in my_points:
            glVertex2f(p[0], p[1])
        glEnd()


def save_drawing(my_lines):
    f = open("drawing.txt", "w")
    f.write(str(len(my_lines)) + "\n")
    for l in my_lines:
        f.write(str(len(l)) + "\n")
        for p in l:
            f.write(str(p[0])+ " " + str(p[1]) + "\n")
    f.close()
    print("Drawing saved")



done = False
init_ortho()
glPointSize(5)
glLineWidth(3)
lines = []
mouse_is_down = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_drawing(lines)
        elif mouse_is_down and event.type == MOUSEMOTION:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))
        elif event.type == MOUSEBUTTONDOWN:
            points = []
            lines.append(points)
            mouse_is_down = True
        elif event.type == MOUSEBUTTONUP:
            mouse_is_down = False


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_lines(lines)
    #plot_graph()

    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
