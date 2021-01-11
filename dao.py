# coding=utf-8
from datetime import datetime
import pytz

import pymongo



myclient = pymongo.MongoClient('mongodb://mongo_server:27017/',tz_aware=True, tzinfo=pytz.timezone('Asia/Shanghai'))

class Dao(object):

    def __init__(self,db_name,table_name):
        self.db_name = db_name
        self.table_name = table_name

    def insert_one(self,t):
        myclient[self.db_name][self.table_name].insert_one(t)

    def insert_many(self,ts):
        myclient[self.db_name][self.table_name].insert_many(ts)

    def delete_one(self,filter):
        myclient[self.db_name][self.table_name].delete_one(filter)

    def delete_many(self,filter={}):
        myclient[self.db_name][self.table_name].delete_many(filter)

    def find(self,filter={}):
        cursor = myclient[self.db_name][self.table_name].find(filter)
        return [ t for t in cursor ]

    def findPage(self,filter,skip,limit):
        cursor = myclient[self.db_name][self.table_name].find(filter).skip(skip).limit(limit)
        return [t for t in cursor]

    def findOne(self):
        return myclient[self.db_name][self.table_name].find_one()



