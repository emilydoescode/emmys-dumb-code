import math

def Circumference(r):
    return 2 * (math.pi) * r

print("Enter Radius of Circle: ", end="")
r = float(input())

c = Circumference(r)
print("\nCircumference = {:.2f}".format(c))