class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def area(self):
        return self.__length*self.__width
    
    def __it__(self,other):
        return self.area() < other.area()
    
r1= Rectangle(10,5)
r2= Rectangle(8,8)

  
if r1 < r2:
    print("rectangle 1 has a smaller area")
else:
    print("rectangle 1 does not have a smaller area")

    
print("area of rectangle 1:",r1.area())
print("area of rectangle 2:",r2.area())