import akshare as ak
from datetime import datetime
from log_utils import log_utils
from dao import Dao
import pytz
from task import Task

log = log_utils.get_logger("fund_task")

class FundTask(Task):

    def excute(self):
        log.info("获取基金的信息")
        fund_em_fund_name_df = ak.fund_em_fund_name()
        dao = Dao("crawler", "fund")
        dao.delete_many({})
        fund_em_fund_name_df["createTime"] = pytz.timezone('Asia/Shanghai').localize(datetime.now())
        fund_em_fund_name_df.rename(
            columns={"基金简称": "name", "基金类型": "fundType", "拼音全称": "fullPinyin", "基金代码": "code", "拼音缩写": "pinyin"},
            inplace=True)
        records = fund_em_fund_name_df.to_dict(orient='records')
        dao.insert_many(records)

        log.info("基金信息获取完毕 共计 %s 条", len(records))



if __name__ == '__main__':
    task = FundTask("task_04")

    task.run()


