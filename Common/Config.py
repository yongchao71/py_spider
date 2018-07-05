'''
@date 2016-8-10
@author: zxy
'''
import configparser
import os
class Config():
    '''
    配置文件操作，confpath配置文件路径
    '''
    #print(os.getcwd())
    #congpath=os.path.dirname(os.path.dirname(os.getcwd()))+"\\config.ini" 
    congpath=os.getcwd()+"\\config.ini"       
    __configParser = configparser.ConfigParser()     
    def __init__(self,congpath=""):
        '''
               构造函数启动
        '''
        if(os.path.exists(congpath) and os.path.isfile(congpath)):
            self.congpath=congpath 
        #print(self.congpath)
        self.__configParser.read(self.congpath)
    def get_sections(self):
        '''
               获取sections，返回为list,不存在则返回[]
        '''
        section = self.__configParser.sections()
        return section
    def get_options(self,section):
        '''
                获取options，返回为list,不存在则返回[]
        '''
        if(self.__configParser.has_section(section)):
            return self.__configParser.options(section)
        return []
    def get_Items(self,section):
        '''
                获取item集合，元祖列表形式，不存在则返回[]
        '''
        if(self.__configParser.has_section(section)):
            return self.__configParser.items(section)
        return []
    def get_Items_Value(self,section,option):
        '''
               获取单个item值，存在则取值，不存在则返回空字符串
        '''
        if(self.__configParser.has_option(section, option)):
            return  self.__configParser.get(section, option)
        return ""
    def add_section(self,section):
        '''
                添加[section]，存在或者添加成功则返回true，否则返回false
        '''
        if(self.__configParser.has_section(section)):
            return True
        try:
            self.__configParser.add_section(section)           
            self.__configParser.write(open(self.congpath,"w"))
            return True
        except:
            return False
    def set_options_Item(self,section,option,value):
        '''
                设置option值，不存在section则返回false，添加成功返回true，添加失败返回false
        '''
        if(not self.__configParser.has_section(section)):
            return False
        try:
            self.__configParser.set(section,option,value)
            self.__configParser.write(open(self.congpath, "w"))
            return True 
        except:
            return False
    def set_Aoptions_Item(self,section,option,value):
        '''
               设置option值，不存在section则创建，添加成功则返回true，添加失败则返回false
        '''
        if(not self.__configParser.has_section(section)):
            if(not self.add_section(section)):
                return False
        if(self.set_options_Item(section, option, value)):
            return True
        return False