class Shop:
    def __init__(self,title, location, openTime, closedTime, sum=0):
        self.sum = sum
        self.title = title
        self.locaiton = location
        self.openTime = openTime
        self.closedTime = closedTime
