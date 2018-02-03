class Color(object):
    def __init__(self,r,g,b,a=0):
        self.rgba_color = (r,g,b,a)
        self.rgb_color = (r,g,b)

    @property
    def r(self):
        return self.rgba_color[0]

    @property
    def g(self):
        return self.rgba_color[1]

    @property
    def b(self):
        return self.rgba_color[2]

    @property
    def a(self):
        return self.rgba_color[3]
