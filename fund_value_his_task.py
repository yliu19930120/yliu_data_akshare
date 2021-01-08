import datetime
from log_utils import log_utils
from task import Task
import akshare as ak
import pytz
from dao import Dao

log = log_utils.get_logger("fundValueHisTask")

class FundValueHisTask(Task):

    def excute(self):

        fund_dao = Dao("crawler", "fund")
        funds = fund_dao.find()
        count = 0
        for fund in funds:
            code = fund['code']
            log.info("爬取基金净 %s 值",code)

            try:
                fund_em_info_df = self.get_one(code)
            except Exception as e:
                log.info("基金 %s 爬取失败 %s ", code,e)
                continue

            fund_em_info_df["createTime"] = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.now())

            fund_em_info_df.rename(
                columns={"净值日期": "date",
                         "单位净值": "value",
                         "累计净值": "cumulativeValue",
                         "日增长率": "growthRate"
                         },
                inplace=True)

            fund_em_info_df["date"] = fund_em_info_df.date.map(
                lambda x: pytz.timezone('Asia/Shanghai').localize(datetime.datetime(x.year, x.month, x.day)))
            numder_func = lambda x: None if x==None else float(x)
            fund_em_info_df["value"] = fund_em_info_df.value.map(numder_func)
            fund_em_info_df["cumulativeValue"] = fund_em_info_df.cumulativeValue.map(numder_func)
            fund_em_info_df["growthRate"] = fund_em_info_df.growthRate.map(numder_func)
            fund_em_info_df["code"] = code

            records = fund_em_info_df.to_dict(orient='records')
            dao = Dao("crawler", "fundValueHis")
            dao.delete_many({"code":code})
            dao.insert_many(records)

            count = count+len(records)

        msg = "基金历史净值爬取完毕总计 %s 条" % count

        return msg

    def get_one(self,code):
        fund_em_info_df = ak.fund_em_open_fund_info(fund=code, indicator="单位净值走势")
        cumu_fund_em_info_df = ak.fund_em_open_fund_info(fund=code, indicator="累计净值走势")

        dffull = fund_em_info_df.merge(cumu_fund_em_info_df,how='outer',on='净值日期')

        return dffull

    def _obj(self):
        return 'fundValueHisTask'


if __name__ == '__main__':
    task = FundValueHisTask('task_05')
    # task.get_one("000002")
    task.excute()