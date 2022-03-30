import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def init_ortho(ortho_width, ortho_depth):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_depth)


def draw_stars(size, color, *args):
    glPointSize(size)
    glColor(*color)
    glBegin(GL_POINTS)
    for idx, star_location in enumerate(args):
        if len(star_location) == 2:
            glVertex2i(star_location[0], star_location[1])
    glEnd()

def get_stars_location_by_matrix(ortho, my_matrix):
    stars = list()
    depth_len = len(my_matrix)
    for j in range(depth_len):
        width_len = len(my_matrix[j])
        for i in range(width_len):
            star_value = my_matrix[j][i]
            if star_value != 0:
                y = ortho[1] - int((j * ortho[1]) / depth_len)  # inverse depth position
                x = int((i * ortho[0]) / width_len)
                stars.append((x,y))

    return stars


A = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1],
    ]

my_ortho = (640, 480)
my_stars = get_stars_location_by_matrix(my_ortho, A)

done = False
init_ortho(*my_ortho)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # draw_stars(5, [1, 1, 0], *[(100, 50), (630, 450)])
    # draw_stars(10, [1, 0, 0], (23, 40), (212, 350))
    draw_stars(5, [1, 1, 0], *my_stars)
    # glPointSize(5)
    # glBegin(GL_POINTS)
    # glVertex2i(100, 50)
    # glVertex2i(630, 450)
    # glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
