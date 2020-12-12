#!/usr/bin/env python3

import tkinter as tk
from time import monotonic as time
import random

from UDPComms import Publisher

RATE = 50 #millis

class Robot:
    def __init__(self, pos):
        self.pos = pos
        self.vel = 0
        self.id = None
        self.dt = RATE/1000

    def update(self):
        self.pos += self.dt * self.vel

    def change_speed(self, step):
        self.vel += step

    def stop(self):
        self.vel = 0 

class Sim:
    def __init__(self):
        self.master = tk.Tk()
        self.canvas = tk.Canvas(self.master, width=800, height=200, bg="white")
        self.canvas.pack()

        self.robot = Robot(200)

        self.master.bind('<Left>',  lambda e: self.robot.change_speed(-1) )
        self.master.bind('<Right>', lambda e: self.robot.change_speed(+1) )
        self.master.bind('<space>', lambda e: self.robot.stop() )

        self.pub = Publisher(8810, "127.0.0.1")

        self.canvas.create_rectangle(0, 100, 800, 200, fill="blue")
        self.canvas.create_rectangle(0, 0, 10, 200, fill="blue")

        self.master.after(0, self.update)
        tk.mainloop()

    def update(self):
        self.robot.update()

        self.publish(self.robot)
        self.plot(self.robot)

        self.master.after(RATE, self.update)

    def publish(self, robot):
        truth = robot.pos
        pos = robot.pos + random.gauss(0, 40)
        vel = robot.vel + random.gauss(0, 5)

        msg = {"truth":truth, "dist": pos, "vel":vel}
        try:
            self.pub.send(msg)
        except:
            pass

    def plot(self, robot):
        if(robot.id != None):
            self.canvas.delete(robot.id)

        robot.id = self.canvas.create_rectangle(robot.pos,        50, 
                                                robot.pos + 100, 100,
                                                fill = "red")

if __name__ == "__main__":
    s = Sim()

