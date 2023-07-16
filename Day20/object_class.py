# class Product:
#     def __init__(self,name):
#         self.name = name

#     def get_name(self):
#         print(f"Product Name is {self.name}")

# p = Product("Laptop")
# p.get_name()


# ------------------------------------------------------


# class GMom:
#     def __init__(self):
#         print("Parent Constructor")

#     def house(self):
#         print("GMom calling")

# class Mom(GMom):
#     def __init__(self):
#         super().__init__()              #recognizes that the class has been inheritated and then goes to the one step up parent class
#         print("Parent Constructor")

#     def house(self):
#         print("Mom calling")

# class Daughter(Mom):                
#     def __init__(self):
#         super().__init__()              #recognizes that the class has been inheritated and then goes to the one step up parent class
#         print("Child Constructor")

#     def house(self):
#         print("Daughter picking")


# d = Daughter()
# d.house()


# ------------------------------------------------------



