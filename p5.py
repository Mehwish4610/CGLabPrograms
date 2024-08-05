import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
pygame.init()
dw =800
dh = 600
display = pygame.display.set_mode((dw, dh), DOUBLEBUF|OPENGL)
pygame.display.set_caption("3D transformation")
glClearColor(0,0,0,1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(45,(dw/dh), 0.1,50.0)
glMatrixMode(GL_MODELVIEW)
vertices = np.array([
    [-1,-1,-1],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1],
    [-1,-1,1],
    [1,-1,1],
    [1,1,1],
    [-1,1,1]
], dtype=np.float32)
edges = np.array([
    [0,1],[1,2],[2,3],[3,0],
    [4,5],[5,6],[6,7],[7,4],
    [0,4],[1,5],[2,6],[3,7]
], dtype=np.uint32)
tm = np.eye(4, dtype= np.float32)
tm[3,:3] = [0,0,-5]
rm = np.eye(4, dtype= np.float32)
sm = np.eye(4, dtype= np.float32)
sm[0,0]=1.5
sm[1,1]=1.5
sm[2,2]=1.5
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMultMatrixf(tm)
    glRotate(angle,1,1,0)
    glMultMatrixf(rm)
    glMultMatrixf(sm)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    angle += 1
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()