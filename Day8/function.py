#Creating first function
""" 
def helloworld():
    print("Hello World")

helloworld()
"""



#Calling using argument in parameter
"""
def hello(name):
    print(f"Hello, {name}!")

hello("Nischal")
"""



#Creating multiple arguments
"""
def person(first_name,last_name,age):
    print(f"My name is {first_name} {last_name}. I am {age} years old.")

person("Nischal", "Dhamala", "23")
"""



#Creating multiple arguments with no sequence but by assigning
"""
def person(first_name,last_name,age):
    print(f"My name is {first_name} {last_name}. I am {age} years old.")

person(last_name = "Dhamala", first_name = "Nischal", age = "23")
"""



#Creating multiple arguments with default value
"""
def info(name, nationality="Nepali"):
    print(f'I am {name} and i am a {nationality}.')

info("Nischal")             #default nationality is Nepali
info("Bhupesh","Indian")    #default value is overrided by "indian"
"""


"""
#creating function with args in array
def child(*kids):
    print(f"My first child name is {kids[0]}. {kids[1]} is my second child while {kids[2]} is our youngest one.")

child ("Susmita","Ram","Suresh")
"""


#using loop to auto print the names
"""
def child(*kids):
    print(f"My kids name are: ")
    for kid in kids: 
        print(kid)        

child ("Susmita","Ram","Suresh","Hari","Binita")
"""



#kwags --> if unknown parameter exits and function need to be made, this comes in handy
#in  dictionary form
"""
def person(**kwags):
    print(kwags)

person(name="Bhupesh")
"""


# printing the dictionary element
"""
def person(**kwags):
    print(kwags["name"])

person(name="Bhupesh")
"""


