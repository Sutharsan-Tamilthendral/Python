base1, height1 = input("Enter base and height of first triangle: ").split()
base1 = int(base1)
height1 = int(height1)

base2, height2 = input("Enter base and height of second triangle: ").split()
base2 = int(base2)
height2 = int(height2)

area1 = (base1*height1)/2
area2 = (base2*height2)/2

if area1 > area2:
    print("Area of triangle 1", area1)
else:
    print("Area of triangle 2", area2)
