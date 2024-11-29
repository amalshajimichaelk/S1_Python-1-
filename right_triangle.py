def rt_triangle(a,b,c):
    if (a**2)+(b**2)==(c**2):
        return True
    return False

tri_sides=[]
num1=int(input("Enter the length of the first side: "))
num2=int(input("Enter the length of the second side: "))
num3=int(input("Enter the length of the third side: "))
tri_sides.append(num1)
tri_sides.append(num2)
tri_sides.append(num3)
tri_sides.sort()
if rt_triangle(tri_sides[0],tri_sides[1],tri_sides[2]):
    print("The given triangle is a right triangle.")
else:
    print("The given triangle is not a right triangle.")