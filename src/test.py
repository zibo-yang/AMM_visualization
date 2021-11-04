# -*- coding: utf-8 -*-
"""
    Animated 3D sinc function
"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys


class Visualizer(object):
    def __init__(self):
        self.traces = dict()
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 40
        self.w.setWindowTitle('pyqtgraph example: GLLinePlotItem')
        self.w.setGeometry(0, 110, 1920, 1080)
        self.w.show()

        # create the background grids
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.w.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.w.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, 0)
        self.w.addItem(gz)

        self.n = 50
        self.m = 50
        self.y = np.linspace(0, 10, self.n)
        self.x = np.linspace(0, 10, self.m)
        self.phase = 0

        for i in range(self.n):
            
            yi = np.array([self.y[i]] * self.m)
            z = np.multiply([self.y[i]], self.x)
            
            #d = np.sqrt(self.x ** 2 + yi ** 2)
            #z = 10 * np.cos(d + self.phase) / (d + 1)
            
            pts = np.vstack([self.x, yi, z]).transpose()
            self.traces[i] = gl.GLLinePlotItem(pos=pts, color=pg.glColor(
                (i, self.n * 1.3)), width=(i + 1) / 10, antialias=True)
            self.w.addItem(self.traces[i])
            
        for i in range(self.m):
           xi = np.array([self.x[i]] * self.n)
           z = np.multiply([self.x[i]], self.y)
           pts = np.vstack([xi, self.y, z]).transpose()
           self.traces[self.n + i] = gl.GLLinePlotItem(pos=pts, color=pg.glColor(
                (i, self.m * 1.3)), width=(i + 1) / 10, antialias=True)
           self.w.addItem(self.traces[self.n + i])
           
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def set_plotdata(self, name, points, color, width):
        self.traces[name].setData(pos=points, color=color, width=width)

    def update(self):
        '''
        for i in range(self.n):
            yi = np.array([self.y[i]] * self.m)
            z = np.multiply([self.y[i]], self.x)
            #d = np.sqrt(self.x ** 2 + yi ** 2)
            #z = 10 * np.cos(d + self.phase) / (d + 1)
            pts = np.vstack([self.x, yi, z]).transpose()
            self.set_plotdata(
                name=i, points=pts,
                color=pg.glColor((i, self.n * 1.3)),
                width=(i + 1) / 10
            )
            self.phase -= .003
            print("data:", pts)
            
        for i in range(self.m):
           xi = np.array([self.x[i]] * self.n)
           z = np.multiply([self.x[i]], self.y)
           pts = np.vstack([xi, self.y, z]).transpose()
           self.set_plotdata(
                name=i+self.n, points=pts,
                color=pg.glColor((i, self.m * 1.3)),
                width=(i + 1) / 10
            )
           self.phase -= .003
         '''
    
    
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(20)
        self.start()


# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    v = Visualizer()
    v.animation()
