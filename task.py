class Ekart:
    def __init__(self):
        self.cart=[]
    
    def add_product(self,name,quantity):
        self.name=name
        self.quantity=quantity
        self.cart.append((self.name,self.quantity))
        print(f"My Cart: {self.cart}")
    
    def remove_product(self,name):
        for i in self.cart:
            if i[0]==name:
                self.cart.remove(i)
                break
        print(f"My Cart after removing product: {self.cart}")
        
    def total_quantity(self):
        self.total=0
        for i in self.cart:
            self.total+=i[1]
        print(f"Total Quantity in Cart: {self.total}")
        

        

user1 = Ekart()
user1.add_product("mobile", 1)
user1.add_product("laptop", 2)
user1.add_product("charger", 3)

user1.total_quantity()

user1.remove_product("laptop")
user1.total_quantity()