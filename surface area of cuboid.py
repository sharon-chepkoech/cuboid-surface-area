import math
import sys
#surface area of a cuboid.
#formula is SA = 2(lh+lw+wh)


length = int(input("Enter the length"))
height = int(input("Enter the height"))
width = int(input("Enter the width"))
 

print("The total surface area is", 2*(length * width + height*length + width*height))
