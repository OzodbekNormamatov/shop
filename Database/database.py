import pymysql
from Domain.shop import Shop

class database:
    def __init__(self):
        self.cursor = pymysql.connect(
            user="root",
            password="root",
            host="localhost"
        )
        self.cur = self.cursor.cursor()
        self.cur.execute("Create database if not exists shop;")
        self.cur.execute("use shop")
        self.cur.execute("""create table if not exists shop(
                        id int auto_increment primary key ,
                        title text,
                        location text,
                        sum real,
                        closed_time text,
                        opened_time text)""")
        self.cur.execute("""create table if not exists product
                         (id int primary key auto_increment,
                         title text,
                         price real,
                         count int,
                         shop_id int);""")


    def selectAllShop(self):
        self.cur.execute("select * from shop")
        return self.cur.fetchall()

    def deleteShop(self,id):
        self.cur.execute(f"delete from shop where id = {id}")
        self.cursor.commit()

    def insertShop(self,shopModel:Shop):
        self.cur.execute(f"""insert into shop(title,location,sum,opened_time,closed_time)
            values("{shopModel.title}","{shopModel.locaiton}",{shopModel.sum},"{shopModel.openTime}","{shopModel.closedTime}");""")
        self.cursor.commit()
    #
    # def selectAllShop(self):
    #     self.cur.execute("select * from shop")
    #     return self.cur.fetchall()
    #
    # def deleteShop(self, id):
    #     self.cur.execute(f"delete shop where id = {id}")
    #
    # def insertShop(self, shopModel: Shop):
    #     self.cur.execute(f"""insert into shop(title,location,sum,opened_time,closed_time)"
    #            values("{shopModel.title}","{shopModel.locaiton}",{shopModel.sum},"{shopModel.openTime}","{shopModel.closedTime}");""")

