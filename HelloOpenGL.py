import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 480, 0)  # for have 0 of depth on top


def draw_stars(size, color, *args):
    glPointSize(size)
    glColor(*color)
    glBegin(GL_POINTS)
    for idx, star_location in enumerate(args):
        if len(star_location) == 2:
            glVertex2i(star_location[0], star_location[1])
    glEnd()


done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glVertex2i(630, 450)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
