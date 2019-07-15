import numpy as np
import matplotlib.pyplot as plt


class Node:
    __count = 0
    def __init__(self, x, y):
        self.__class__.__count += 1
        self.n = self.__class__.__count 
        self.x = x
        self.y = y

    def viz(self, show_tag: bool = True):
        plt.plot([self.x], [self.y])
        if show_tag:
            plt.text(self.x, self.y, f"n{self.n}")


class Element:
    __count = 0
    def __init__(self, s: Node, e: Node):
        self.__class__.__count += 1
        self.n = self.__class__.__count 

        self.start = s
        self.end = e

    @property
    def length(self):
        dx = self.start.x - self.end.x
        dy = self.start.y - self.end.y
        return np.sqrt(dx ** 2 + dy ** 2)

    def center(self):
        xc = (self.start.x + self.end.x)/2
        yc = (self.start.y + self.end.y)/2

        return xc, yc

    def viz(self, show_tag: bool = True):
        plt.plot([self.start.x, self.end.x], [self.start.y, self.end.y], 'b')
        self.start.viz(show_tag=show_tag)
        self.end.viz(show_tag=show_tag)
        if show_tag:
            plt.text(*self.center, f"({self.n})")


class Truss:
    def __init__(self, *elements):
        self.elements = elements

    def show(self):
        for el in self.elements:
            el.viz()
        plt.show
        