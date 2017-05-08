import sys, os
import time
import pygame
import random
import math


class MouseControl(object):
    def __init__(self):
        pass
    def getmouseinfo(self):
        """Get mouse info such as position, velocity(Currently Unavailable)"""
        mouse_pos = pygame.mouse.get_pos()
        mouseinfo = {
        "mouse_x" : mouse_pos[0],
        "mouse_y" : mouse_pos[1]
        }
        return mouseinfo
