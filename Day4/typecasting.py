
"""
#float value
pi = 3.14

new_pi=int(pi)      #converting float into int
print(new_pi)

print(type(new_pi))

str_pi = str(pi)    #converting float into str
print(type(str_pi))

"""


"""my_list=[1,2,3,4]

my_tuple=tuple(my_list)
print(my_tuple)"""


#Change an element of tuple
my_tuple=("sun","moon",5)
into_list=list(my_tuple)
print(type(into_list))

into_list[2]=4              #after converting, changing the value of 5 into 4
my_tuple=tuple(into_list)
print(my_tuple)


my_string='12'
print(int(my_string))