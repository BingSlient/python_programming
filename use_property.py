"""Learn how to use @property function in python
"""

class Screen(object):
    def __init__(self, w, h):
        self.__width = w
        self.__height = h
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, h):
        self.__height = h
    
    @property
    def resolution(self):
        return self.__width * self.__height

if __name__ == "__main__":
    s = Screen(1900, 1080)
    print('screen s:\nwidth:{},height:{},resolution:{}'\
          .format(s.width, s.height, s.resolution))

    s.width = 1080
    s.height = 720
    print('setting screen s with:\nwidth:{},height:{},resolution:{}'\
          .format(s.width, s.height, s.resolution))