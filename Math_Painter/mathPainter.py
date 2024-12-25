# Includes all class requried for Math Painter app.
import numpy as np
from PIL import Image


class Canvas:
    ''' Object where all shapes are going to be drawn'''

    def __init__(self, length, width, color):
        self. length        = length
        self.width          = width
        self.color          = color

        # Create a 3d canvas with numpy array.
        # Here length and width as user provides.
        # for z axis = 3, its for 3 layers of basic colors Red, green, blue.
        self.canvas3D = np.zeros((self.length, self.width, 3), dtype=np.uint8)

        # Assigning either black or white color to canvas
        self.canvas3D[:] = self.color


    def make_canvas(self, imagepath):
        """
            Function which draws canvas i.e. converts the current array to Image.
        """
        img = Image.fromarray(self.canvas3D, 'RGB')
        img.save(imagepath)


class Rectangle:


    def __init__(self, x_coordinate, y_coordinate, length, width, color):
        self.x_coordinate   = x_coordinate
        self.y_coordinate   = y_coordinate
        self.length        = length
        self.width          = width
        self.color          = color
    

    def draw_rect(self, canvas_obj):
        """
            Method which draws rectangle using canvas.
        """
        canvas_obj.canvas3D[self.x_coordinate:(self.x_coordinate+self.length), self.y_coordinate:(self.y_coordinate+self.width)] = self.color



class Square:


    def __init__(self, x_coordinate, y_coordinate, side, color):
        self.x_coordinate   = x_coordinate
        self.y_coordinate   = y_coordinate
        self.side           = side
        self.color          = color
    

    def draw_sqr(self, canvas_obj):
        """
            Method which draws square using canvas.
        """
        canvas_obj.canvas3D[self.x_coordinate:(self.x_coordinate+self.side), self.y_coordinate:(self.y_coordinate+self.side)] = self.color





