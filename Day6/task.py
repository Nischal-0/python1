#-----------------------------------------------------------------------------------
#Create variable user and password and initialize with value and take input from user if it is valid or not
#-----------------------------------------------------------------------------------
"""
email = "nis@gmail.com"
pwd = "Nep@l1"

name = input("Enter a username: ")

mail = input("Enter your Mail id: ")
pswd = input("Enter Password: ")

if (mail == email and pswd == pwd):
    print(f"The user {name} has been logged in.")
else:
    print(f"Mail id or Password is incorrect for {name}.")

"""

#-----------------------------------------------------------------------------------
#fetch 'h' from "Rohan" 
#-----------------------------------------------------------------------------------
"""
a = {"name" : ["Sisir",
        "Nitish",
        "Nischal",
        "Rohan"
        ]
    }

fetch = a['name'][3][2]     #fetch name and then 3rd index. 2nd index from the output of 3rd index is finally fetched for output 
print(fetch) 
"""

#-----------------------------------------------------------------------------------
#From the given text, print the reverse form and print "World" only
#-----------------------------------------------------------------------------------
"""
country = "Hello World"
print(country[::-1])    #"::" means 
print(country[-5:])
"""


#-----------------------------------------------------------------------------------
#In my_tuple=(1,2,3,4,5), change '2' into '11'.
#-----------------------------------------------------------------------------------
"""
my_tuple=(1,2,3,4,5)
new = list(my_tuple)
new[1] = 11
my_tuple = tuple(new)
print(my_tuple)
print(type(my_tuple))
"""