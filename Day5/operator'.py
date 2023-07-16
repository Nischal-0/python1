'''a=5
b=2
sum = a+b
substract = b-a
multiply = a*b
divide = a/b
modulus=a%b
exponential=a**b
print("The Sum is = ", sum)
print("The Difference is = ", substract)
print("The Multiple is = ", multiply)
print("The Division is = ", divide)
print("The Modulus is = ", modulus)
print("The Exponential is = ", exponential)
'''


"""
#assignment operator

a=10

a+=1
print(a)

a-=1
print(a)

a*=1
print(a)

a/=1
print(a)

a%=1
print(a)

a//=1
print(a)

a**=1
print(a)

"""

"""
#Comparison Operator

a=10
b=10

print (a==b)


a=5
b=4

print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
"""

"""
#Logical operator

a=3
b=4

print(a<10 and b<10)        #if both is true then whole statement is true

print (a<b or b>a)          #if at least one is true then whole statement is true

print (not(a<b or b>a))     #if statement is true, output is false & visa versa


"""


"""a=4

print(a%2==0)"""


"""isLogin = True
isAuthorized = True

print(isLogin and isAuthorized)
"""



a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

op = int(input("""
1. Sum
2. Substract
3. Multiple
4. Divide
5. Modulus
6. Exponential

Which operator you want to perform?: """))

sum = a+b
substract = b-a
multiply = a*b
divide = a/b
modulus=a%b
exponential=a**b

if(op == 1):
    print("The Sum is = ", sum)
elif(op == 2):
    print("The Difference is = ", substract)
elif(op == 3):
    print("The Multiple is = ", multiply)
elif(op == 4):
    print("The Division is = ", divide)
elif(op == 5):
    print("The Modulus is = ", modulus)
elif(op == 6):
    print("The Exponential is = ", exponential)
else:
    print("Invalid Input")

option=input("Do you want to perform the operation again[Y/N]: ")

    



