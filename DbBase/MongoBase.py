'''
@date 2016-8-10
@author: zxy
'''
import Common.Config as Config  #导入配置文件
import pymongo  #mongo数据库模块
import os
from bson import ObjectId #处理bsonid {'_id': ObjectId('57aaf52567650660a0ac4b69')}
class MongoBase():
    #__configFile=os.path.dirname(os.path.dirname(os.getcwd()))+"\\config.ini"
    __configFile=os.path.dirname(os.getcwd())+"\\config.ini"
    __config=Config.Config(__configFile)
    __server=__config.get_Items_Value("mongodb","db_host")
    __port=int(__config.get_Items_Value("mongodb","db_port"))
    def __init__(self,server=__server,port=__port):
        self.__client = pymongo.MongoClient(server,port)     
    def __del__(self):
        self.__client.close()
    def get_mclient(self):
        '''
        获取连接客户端
        '''
        return self.__client
    def convertBson(self,data):
        '''
        bson处理，用于提取id字段
        '''
        return ObjectId(data)
        