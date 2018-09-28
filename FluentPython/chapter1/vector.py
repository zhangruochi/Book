from math import hypot

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({},{})'.format(self.x,self.y)    

    
    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))
        #return bool(self.x or self.y)

    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    
    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar)


if __name__ == '__main__':
    print(Vector(3,4))
    print(abs(Vector(3,4)))
