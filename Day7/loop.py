#WHILE LOOP

#print from 1 to 10

#using no if statement
"""i = 1
while i <= 10:
    while i%2==0:
        print (i)
        break       #to break the loop and go to next line
    i+=1"""

#using if statement
"""i=1
while i<=10:
    if i%2==0:
        print (i)
    i+=1"""



#continue statement
"""
i=0
while i<=10:
    print(i)
    if i == 5:
        continue      #goes back top of the loop, so it will not skip number five.
    i+=1
"""

#"in" keyword
"""a = [1,2,3,5]
print(4 in a)
"""

#range keyword
"""
a = range(10)
print(a)        #notifies the range from 0 to 10
my_list = list(a)
print(my_list)  #prints the range from 0 to 10
"""

#FOR LOOP
"""
for i in range(10):
    print(i)
"""


alphabets=['a','b','c']
for set in alphabets:
    print (set)


a="Hello World"
for char in a:
    print(char)        #output comes in loop print of the above statement because it is string array of character