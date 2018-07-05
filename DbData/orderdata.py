from DbBase.MongoBaseImpl import MongoBaseImpl
import datetime
import random
class OrderData:   
    def __init__(self):
        self.datehandle=MongoBaseImpl("mydb","users")
    def order_list(self):
        return self.datehandle.find()
    def order_add_item(self):
        time=random.uniform(10, 2000)   
        orderitem={'name':time,'age':223,'sex':True}
        return self.datehandle.insert(orderitem)
    def order_item_get(self):
        return self.datehandle.findOne()
    def order_item_del(self,itemid):
        itemid=self.datehandle.convertBson(itemid)
        deldata={"_id":itemid}
        return self.datehandle.remove(deldata)