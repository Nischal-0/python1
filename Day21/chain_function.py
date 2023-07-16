# class Burger:

#     def bun(self):
#         print("Bun is ready")
#         return self

#     def patty(self):
#         print("Patty is ready")
#         return self

#     def sause(self):
#         print("Sauce is ready")
#         return self

#     def mayo(self):
#         print("Mayo is ready")
#         return self

#     def salad(self):
#         print("Salad is ready")
#         return self


# b = Burger()
# b.bun().patty().sause().mayo().salad()


# ---------------------------------------------------------------------------------




class Pizza:
    
    def dough(self):
        print("Dough is smooth and ready")
        return self

    def sause(self):
        print("Sause is red and ready")
        return self
        
    def toppings(self):
        print("Toppings is added")
        return self
    
    def veggies(self):
        print("Veggies is added")
        return self

p = Pizza()
p.dough().sause().veggies().toppings()

