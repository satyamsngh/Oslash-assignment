from additionals import shopkeeper

class item:

    def __init__(self, name, category, price, discount):
        self._name = name
        self._category = category
        self._price = price
        self._discount = discount
        self.__max_quantity = shopkeeper.ClothingMaxQuantity if category == shopkeeper.Clothing else shopkeeper.StationeryMaxQuantity
    
    @classmethod
    def fromStr(cls, string):
        _name, _category, _price, _discount = string.split()
        return cls(_name, _category, int(_price), int(_discount))
    
    def getName(self):
        return self._name
    
    def getCategory(self):
        return self._category
    
    def getPrice(self):
        return self._price
    
    def getDiscount(self):
        return self._discount
    
    def getMaxQuantity(self):
        return self.__max_quantity

class inventory():
    
    def __init__(self, inventoryList):
        self.__total = shopkeeper.empty
        self._discount = shopkeeper.empty
        self.__bill = ""
        self.__product = []
        self.__setProducts(inventoryList)
        
    def __setProducts(self, inventoryList):
        inventoryList = inventoryList.split (shopkeeper.newLine)
        for object in inventoryList:
            self.__product.append(item.fromStr(object))

    def __addProducts(self, name, quantity):

        for product in self.__product:
            
            if product.getName() == name:

                if quantity > product.getMaxQuantity():
                    return shopkeeper.error

                else:
                    self.__total += product.getPrice() * quantity
                    self._discount += product.getPrice() * quantity * product.getDiscount() / shopkeeper.maxDiscount

                    return shopkeeper.success

    def __setTotalAndDiscount(self):

        if self.__total >= shopkeeper.minDiscountThreshold:
            self.__total -= self._discount
        else:
            self._discount = shopkeeper.empty

        if self.__total >= shopkeeper.extraDiscountThreshold:
            self._discount += self.__total * shopkeeper.extraDiscount
            self.__total -= self.__total * shopkeeper.extraDiscount
        self.__total += self.__total * shopkeeper.taxPercentage

    def __generateBill(self, orders):
            
            for order in orders:
    
                if order.startswith (shopkeeper.addItem):
                    action, item, quantity = order.split()
                    self.__bill += self.__addProducts(item, int(quantity))
    
                else:
                    self.__setTotalAndDiscount()
                    self.__bill += shopkeeper.billFormatter(self._discount, self.__total)
                    
    
    def getBill(self, orders):
        self.__generateBill(orders)
        
        return self.__bill



