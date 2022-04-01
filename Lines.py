import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *
pygame.init()

screen_width = 1000
screen_height = 800
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


def plot_point(my_points):
    glBegin(GL_POINTS)
    for p in my_points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines(my_lines):
    for my_points in my_lines:
        glBegin(GL_LINE_STRIP)
        for p in my_points:
            glVertex2f(p[0], p[1])
        glEnd()


done = False
init_ortho()
glPointSize(5)

lines = []
mouse_is_down = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif mouse_is_down and event.type == MOUSEMOTION:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                           map_value(0, screen_height, ortho_height, 0, p[1])))
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

    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
