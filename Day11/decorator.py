

def dash(func):
    def wrapper():
        print("-" * 10)
        func()
        print("-" * 10)
    return wrapper

def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper

def per(func):
    def wrapper():
        print("%" * 10)
        func()
        print("%" * 10)
    return wrapper


@dash
@star
@per

def shout():
    print("Hi.")


shout()



# dash(shout) ()
# per(shout) ()
# star(shout) ()


"""
def func(funtion):
    funtion()

def hello_world():
    print("Hello World")

#call back function
func(hello_world)
"""




