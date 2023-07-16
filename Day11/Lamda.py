#lamda function

"""
x = lambda a: a + 10        # ":" inside the function and firstly written "a" is the parameter here and a + 1 is return value
print(x(1)) 
"""

"""
sum = lambda a,b: a+b
print(sum(2,8))
"""


"""
area = lambda l,b: l*b
print(f"The area of rectangle is: ", area(2,9))
"""


def function(n):
    return lambda a: a*n

double=function(2)
triple=function(3)

"""
d = int(input("\nEnter the number you want to double: "))
t = int(input("\nEnter the number you want to triple: "))
print(f"\nMultiple of {d} is:", double(d))
print(f"\nMultiple of {t} is:", triple(t))
print("\n")
"""


def function(n):
    return lambda a: a*n

times4 = function(4)

f = int(input("Enter a number you want to times 4 with: "))
print(f"Fourth Multiple of {f} is: ", times4(f))
print("\n")