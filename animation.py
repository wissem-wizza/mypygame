import pygame
import os
import time
import spriteSheet

class Animation:

    def __init__(self, frames, speed):
        # fileName,columns,rows,flipped
        self.frames = frames
        # print("init animation class: " + str(len(self.frames[0])))
        self.speed = speed
        self.index , self.lastTime , self.currentTime , self.timer = 0,0,0,0
        self.animating = True
        


    def tick(self):

        if self.animating == True:
            self.currentTime = time.time()
            self.timer = self.currentTime - self.lastTime
            if self.timer > self.speed:
                self.lastTime = self.currentTime
                self.timer = 0
                if self.index < len(self.frames)-1:
                    self.index+=1
                else: self.index = 0

    def getCurrentFrame(self):
        return self.frames[self.index]