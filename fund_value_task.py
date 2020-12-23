from datetime import date
from datetime import datetime
from log_utils import log_utils
from task import Task
import akshare as ak
import pytz
from dao import Dao

log = log_utils.get_logger("fundValueTask")

class FundValueTask(Task):

    def excute(self):
        dao = Dao("crawler", "fund")
        fund_em_open_fund_daily_df = ak.fund_em_open_fund_daily()
        fund_em_open_fund_daily_df["createTime"] = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.now())
        print(fund_em_open_fund_daily_df.columns.values)

        today = date.today()
        lastday = today_key.replace(day=today_key.day-1)
        todayKey = date.today().strftime('%Y-%m-%d')
        lastdayKey = today_key.replace(day=today_key.day-1).strftime('%Y-%m-%d')


        fund_em_open_fund_daily_df.rename(
            columns={"基金简称": "name",
                     "申购状态": "subscribeType",
                     "赎回状态": "redemptionType",
                     "基金代码": "code",
                     "手续费": "fee",
                     "日增长值": "growthValue",
                     "日增长率": "growthRate",
                     },
            inplace=True)

        records = fund_em_open_fund_daily_df.to_dict(orient='records')

        # dao.insert_many(records)

        msg = "基金净值信息获取完毕 共计 %s 条" % len(records)
        log.info(msg)
        return msg

    def _obj(self):
        return 'fundValueTask'


if __name__ == '__main__':
        # task = FundValueTask('task_004')
        #
        # task.excute()
        today_key = date.today()
        lastdayKey = today_key.replace(day=today_key.day-1).strftime('%Y-%m-%d')
        print(today_key,lastdayKey)