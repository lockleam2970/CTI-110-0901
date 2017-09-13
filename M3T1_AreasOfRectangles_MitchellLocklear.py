# M3T1
# Areas of Rectangles
# Mitchell Locklear
# 09/13/2017

height1 = int(input("What is the HEIGHT of the FIRST rectangle: "))
width1 = int(input("What is the WIDTH of the FIRST rectangle: "))
height2 = int(input("What is the HEIGHT of the SECOND rectangle: "))
width2 = int(input("What is the WIDTH of the SECOND rectangle: "))

area1 = height1*width1
area2 = height2*width2

if area1 > area2:
    print("The FIRST rectangles area is greater!")
    
if area2 > area1:
    print("The SECOND rectangles area is greater!")

if area1 == area2:
    print("The Rectangles have the same area!")
