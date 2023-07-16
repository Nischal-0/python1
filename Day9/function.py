#pass is a keyword which is used when nothing is needed

"""
def hello_world():
    return "Hello World"

value=hello_world()

print(value)
"""


"""
def calculate(n):
    o=n*10
    res=o/2
    return res

result=calculate(5)

print(result)
"""



def check(usname,pswd):
    if (usname == 'admin' and pswd=='admin'):
        return True
    else : 
        return False


"""
if (usname == 'admin' and pswd=='admin'):
        return True
    else : 
        return False
"""

#this can be minimized into 

#return usname == 'admin' and pswd=='admin'\


def login(usnam,pswd):
    if check(usnam,pswd):
        print('Login Successful')
    else:
        print('IMPOSTER')


usn = input("enter username: ")
pswd = input("enter password: ")
login(usn,pswd)
