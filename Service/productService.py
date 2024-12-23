

class productService:
    def __init__(self):

    def addProduct(self, count):
        self.count += count

    def saleProduct(self, count):
        self.count -= count

    def updatePrice(self, price):
        self.price = price

    def getInfo(self):
        print(f"""
               Product name: {self.title}
               Product price : {self.price}
               Product count : {self.count}
               """)

