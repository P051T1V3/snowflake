class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x:{self.x} y:{self.y}"

    def mid_point(self,point,prc,n_prc):
        new_x = self.x * n_prc + point.x * prc
        new_y = self.y * n_prc + point.y * prc
        return Point(new_x, new_y)
