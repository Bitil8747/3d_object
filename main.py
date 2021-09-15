################################################################################ Рисуем градиент
#from PIL import Image
#
#img = Image.new('RGB',(255,255),"Black")
#pixels = img.load()
#
#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        pixels[i,j] = (255-i,j,50)
#
#img.show()


################################################################################# Рисуем диагональную линию
#from PIL import Image
#
#x = 800
#y = x
#img = Image.new('RGB',(x,x),"Black")
#pixels = img.load()
#color = (255,255,255)
#
#for j in range(x):
#    for i in range(x):
#        pixels[i,i] = color
#
#img.show()


################################################################################### 3d объекты
#from PIL import Image
#import re
#
#scr_x = 800
#scr_y = scr_x
#half_x = int(scr_x / 2)
#half_y = int(scr_y / 2)
#img = Image.new('RGB',(scr_x+1,scr_y+1),"Black")
#pixels = img.load()
#color = (255,255,255)
#
#f = open("C:\\Users\Airat\Desktop\Sphere.obj",'r')
#lines = f.read()
#for i in lines.split('\n'):
#   try:
#        v, x, y, z = re.split('\s+', i)
#    except:
#        continue
#    if v == 'v':
#        x = int((float(x) + 1) * half_x)
#        y = scr_y - int((float(y) + 1) * half_y)
#        print(x,y)
#        #pixels[x, y] = color
#
#class Point(object):
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#
#    def show(self,color=None):
#        pixels[self.x,scr_y - self.y] = color or (255,255,255)
#
#Point(20,30).show()
#img.show()


############################################################################################
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import pygame
import os

from pygame.locals import *
from constants import *
from MeshRenderer import CubeMesh, ChairMesh


os.environ["SDL_VIDEO_CENTERED"]='1'


def random_color():
    x = random.randint(0, 255) / 255
    y = random.randint(0, 255) / 255
    z = random.randint(0, 255) / 255
    color = (x, y, z)
    return color

colors_list= []

for n in range(len(chair_faces_vector4)):
    colors_list.append(random_color())


def main():
    pygame.init()
    display = (900, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)
    glRotatef(-90, 1, 0, 0)


main()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glRotatef(3, 0, 0, -45)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    ChairMesh()
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
quit()