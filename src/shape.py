import math

# Point Class:
class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}' # print(...) also returns 'None' so it should be returned as a string
    
    def __add__(self, p2) -> float:
        return Point(self.x + p2.x, self.y + p2.y)
    
    def __sub__(self, p2) -> float:
        return Point(self.x - p2.x, self.y - p2.y)
    
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
# Shape Class:
class Shape:
    def __init__(self) -> None:
        self.vertices = []
        
    def add_vertex(self, p:Point) -> None:
         self.vertices.append(p)
            
    def __str__(self) -> str:
        return f'number of vertices: {len(self.vertices)}'
    
    def perimeter(self) -> float:
        # if the shape has no vertices, the perimeter may not be calculated
        if len(self.vertices) == 0:
            raise RuntimeError("Shape does not have vertices")
            
        p = 0
        for i in range(len(self.vertices)):
            # if it's a line:
            if len(self.vertices) == 2:
                p += math.sqrt((self.vertices[1].x - self.vertices[0].x)**2 + (self.vertices[1].y - self.vertices[0].y)**2)
                return p
            
            if i == len(self.vertices)-1:
                p += math.sqrt((self.vertices[i].x - self.vertices[0].x)**2 + (self.vertices[i].y - self.vertices[0].y)**2)
            else:
                p += math.sqrt((self.vertices[i].x - self.vertices[i+1].x)**2 + (self.vertices[i].y - self.vertices[i+1].y)**2)
        return p
         
# Line Class:
class Line(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        Shape.__init__(self)
        self.vertices.append(p1)
        self.vertices.append(p2)
        
    def __str__(self) -> str:
        s = f''' Line:
 	p1: ({self.vertices[0]})
 	p2: ({self.vertices[1]})'''
        return s
    
    def area(self) -> float:
        return 0

# Triangle Class:
class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point) -> None:
        Shape.__init__(self)
        self.vertices.append(p1)
        self.vertices.append(p2)
        self.vertices.append(p3)
        # Either check if they're all on the same line (bad approach)
        if ((p1.x == p2.x) and (p2.x == p3.x)) or ((p1.y == p2.y) and (p2.y == p3.y)):
            raise RuntimeError("Shape is not a triangle")
        # Or check if the area is zero (better approach)
        if self.area() == 0:
            raise RuntimeError("Shape is not a triangle")

    def __str__(self) -> str:
        s = f''' Triangle:
 	p1: ({self.vertices[0]})
 	p2: ({self.vertices[1]})
 	p3: ({self.vertices[2]})'''
        return s
    
    def area(self) -> float:
        p = self.perimeter()/2
        # Calculate the length of each side
        len_a = math.sqrt((self.vertices[0].x - self.vertices[1].x)**2 + (self.vertices[0].y - self.vertices[1].y)**2)
        len_b = math.sqrt((self.vertices[1].x - self.vertices[2].x)**2 + (self.vertices[1].y - self.vertices[2].y)**2)
        len_c = math.sqrt((self.vertices[2].x - self.vertices[0].x)**2 + (self.vertices[2].y - self.vertices[0].y)**2)
        a = math.sqrt(p*(p-len_a)*(p-len_b)*(p-len_c))
        return a

        
# Rectangle Class:
class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        Shape.__init__(self)
        point1 = Point(p1.x, p2.y)
        point2 = p2
        point3 = Point(p2.x, p1.y)
        point4 = p1
        self.vertices.append(point1)
        self.vertices.append(point2)
        self.vertices.append(point3)
        self.vertices.append(point4)
        
    def __str__(self) -> str:
        s = f''' Rect:
 	p1: ({self.vertices[0]})
 	p2: ({self.vertices[1]})
 	p3: ({self.vertices[2]})
 	p4: ({self.vertices[3]})'''
        return s
        
    def area(self) -> float:
        a = (self.vertices[1].x - self.vertices[0].x) * (self.vertices[2].y - self.vertices[1].y)
        return abs(a)
        
# EOF