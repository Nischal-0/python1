#global variable in function
"""
a = 10

def call():
    print(a)

call()
"""



#converting local into global variable in function
"""
def local_call():
    global a
    a=10

local_call()
print(a)
"""



def parent():
    a = 26
    def child():
        print(a)
    child()

parent()


