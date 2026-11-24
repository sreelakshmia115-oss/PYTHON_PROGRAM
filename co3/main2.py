from graphics import circle,rectangle
from graphics.t3D_graphics import cuboid,sphere

print("circle operations")
print("area of circle=",circle.area(5))
print("perimeter of circle=",circle.perimeter(6))


print("rectangle operations")
print("area of rectangle=",rectangle.area(4,6))
print("perimeter of rectangle=",rectangle.perimeter(5,7))

print("cuboid operations")
print("surfacearea of cuboid=",cuboid.surfacearea(3,4,5))
print("perimeter of cuboid=",cuboid.perimeter(3,4,5))

print("sphere operations")
print("area of sphere=",sphere.area(6))
print("volume of sphere=",sphere.volume(5))