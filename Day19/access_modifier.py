class Product:
    name = "Mic"                #public attribute 
    _price = 299                #protected attribute with "_" as starting character
    __category ="Sound"         #private attribute with "__" as starting character


    @property                       #Getter method - has return
    def category(self):
        return self.__category
    
    @category.setter                #Setter method - has no return
    def category(self,value):
        self.__category.value


p = Product()

p.__category = "audio"      #accessing the private attribute after creating the object 

print(p.__category)

