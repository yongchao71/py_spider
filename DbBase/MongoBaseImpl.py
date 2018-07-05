'''
@date 2016-8-10
@author: zxy
'''
from DbBase.MongoBase import MongoBase
#from bson import ObjectId
class MongoBaseImpl(MongoBase): 
    def __init__(self,db,collection):
        MongoBase.__init__(self)
        self.__client=self.get_mclient()
        self.db=self.__client[db]
        self.collection=self.db[collection]
    def usedb(self,dbname):
        '''
        切换数据库
        '''
        self.db=self.__client[dbname]
    def useTable(self,collection):
        '''
        切换表
        '''
        self.collection=self.db[collection]
    def find(self,query={}):
        '''
        查找多条数据
        '''
        if type(query) is not dict:
            return []
        try:
            result=[]
            items=self.collection.find(query)
            for item in items:
                result.append(item)             
            return result
        except:
            return []
    def findOne(self,query={}):
        '''-9+6
        查找单条数据
        '''
        if type(query) is not dict:
            return {}
        try:
            result=self.collection.find_one(query)
            return result
        except:
            return {}
    def insert(self,data={}):
        '''
        插入数据
        '''
        if type(data) is not dict:
            return False
        try:
            self.collection.insert(data)
            return True
        except:
            return False 
    def insertOne(self,data={}):
        '''
        插入单条数据并返回插入id
        '''
        if type(data) is not dict:
            return -1
        try:
            result=self.collection.insert_one(data).inserted_id
            return result
        except:
            return -1
    def remove(self,params={}):
        '''
        删除数据
        '''
        if type(params) is not dict:
            return False
        try:
            self.collection.remove(params)
            return True
        except:
            return False
    def update(self, data={}, setdata={},multidata=False):
        '''
        根据条件更新数据，data查找条件,setdata设置条件，multidata是否多条
        '''
        if type(data) is not dict or type(setdata) is not dict:
            return False
        try:
            self.collection.update(data,{'$set':setdata},upsert=False, multi=multidata)
            return True
        except:
            return False
    def count(self,params={}):
        '''
        获取数量，不传默认获取全部数量
        '''
        if type(params) is not dict:
            return 0
        try:
            count=self.collection.count(params)
            return count
        except:
            return 0
