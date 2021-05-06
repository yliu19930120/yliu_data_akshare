from dao import Dao
from task import Task
import pandas as pd
import os
import datetime
import pytz
class DigitalTask(Task):


    def excute(self):
        root = 'F:\\学习资料\\回测系统构建\\binance_1m_data\\'
        files = os.listdir(root)
        dao = Dao('crawler', 'sourceAssetValue')

        for file in files:
            if 'BTCUSDT' not in file:
                continue
            data = pd.read_csv(root+file)
            data["create_time"] = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.now())
            records = data.to_dict(orient='records')
            dao.insert_many(records)
            print(len(data))

        return '读取完毕'

if __name__ == '__main__':
    task = DigitalTask("","")
    task.excute()