#--------------------------------------------------------------------------
#Top down VTMB type shooter project. Let's keep this simple.
#Focuses, Goals
#1.Basic Control
#2.Sounds
#3.Dialogues
#4.3D Sounds
#5.Levels

import sys, os
import time
import pygame
import random
import math

import gamesys
import controls

#Pre-define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_W = 700
screen_H = 550

mousecontrol = controls.MouseControl()

class Cursor(pygame.sprite.Sprite):

    def __init__(self, cursor_location = None, cursor_image = None):
        super().__init__()
        self.mouseinfo = mousecontrol.getmouseinfo()
        self.image = pygame.image.load(os.path.join(cursor_location, cursor_image)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.mouseinfo["mouse_x"]
        self.rect.y = self.mouseinfo["mouse_y"]
    def update(self):
        self.mouseinfo = mousecontrol.getmouseinfo()
        self.rect.x = self.mouseinfo["mouse_x"]
        self.rect.y = self.mouseinfo["mouse_y"]

def main():

    pygame.init()

    """System Section"""
    done = False

    clock = pygame.time.Clock()

    """Paths"""
    current_path = os.path.dirname(__file__)
    data_path = os.path.join(current_path, 'data')
    graphics_path = os.path.join(data_path, 'graphics')

    frame_manager = gamesys.FrameManager()

    """Check for saves and config"""
    file_manager = gamesys.FileManager()
    file_manager.check_files(data_path)

    """Controls"""
    mousecontrol = controls.MouseControl()


    """Graphics Section"""
    all_sprites_list = pygame.sprite.Group()

    screen = pygame.display.set_mode([screen_W, screen_H])

    cursor = Cursor(graphics_path, "cursor_lips.png")
    all_sprites_list.add(cursor)

    while not done:
        frame_manager.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        cursor.update()

        screen.fill(WHITE)

        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)
if __name__ == "__main__":
    main()
