# coding=utf-8
from datetime import datetime

import pymongo



myclient = pymongo.MongoClient('mongodb://mongo_server:27017/')

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

    def delete_many(self,filter):
        myclient[self.db_name][self.table_name].delete_many(filter)

    def find(self,filter):
        cursor = myclient[self.db_name][self.table_name].find(filter)
        return [ t for t in cursor ]

    def find(self,filter,skip,limit):
        cursor = myclient[self.db_name][self.table_name].find(filter).skip(skip).limit(limit)
        return [t for t in cursor]

if __name__ == '__main__':
    fund_em_fund_name_df = ak.fund_em_fund_name()
    dao = Dao("crawler", "fund")
    dao.delete_many({})
    fund_em_fund_name_df["createTime"] = datetime.now()
    fund_em_fund_name_df.rename(columns={"基金简称": "name", "基金类型": "fundType", "拼音全称": "fullPinyin", "基金代码": "code", "拼音缩写": "pinyin"}, inplace=True)
    records = fund_em_fund_name_df.to_dict(orient='records')

    dao.insert_many(records)

