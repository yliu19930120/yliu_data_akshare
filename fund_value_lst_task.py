from datetime import date
import datetime
from log_utils import log_utils
from task import Task
import akshare as ak
import pytz
from dao import Dao

log = log_utils.get_logger("fundValueLstTask")

class FundValueLstTask(Task):

    def excute(self):
        dao = Dao("crawler", "fundValueLst")
        fund_em_open_fund_daily_df = ak.fund_em_open_fund_daily()
        fund_em_open_fund_daily_df["createTime"] = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.now())


        today = date.today()
        lastday = today.replace(day=today.day-1)
        todayKey = date.today().strftime('%Y-%m-%d')
        lastdayKey = lastday.strftime('%Y-%m-%d')

        keys = fund_em_open_fund_daily_df.keys()

        if "%s-累计净值" % todayKey not in keys:
            msg = "%s 净值 不存在" % todayKey
            log.info(msg)
            return msg

        fund_em_open_fund_daily_df.rename(
            columns={"基金简称": "name",
                     "申购状态": "subscribeType",
                     "赎回状态": "redemptionType",
                     "基金代码": "code",
                     "手续费": "fee",
                     "日增长值": "growthValue",
                     "日增长率": "growthRate",
                     "%s-累计净值" % todayKey: "cumulativeValue",
                     "%s-单位净值" % todayKey: "value",
                     "%s-累计净值" % lastdayKey: "cumulativeValuePrev",
                     "%s-单位净值" % lastdayKey: "valuePrev"
                     },
            inplace=True)

        fund_em_open_fund_daily_df["date"] = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.strptime(todayKey,'%Y-%m-%d'))
        fund_em_open_fund_daily_df["datePrev"] = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.strptime(lastdayKey,'%Y-%m-%d'))

        records = fund_em_open_fund_daily_df.to_dict(orient='records')

        dao.insert_many(records)

        msg = "基金净值信息获取完毕 共计 %s 条" % len(records)
        log.info(msg)
        return msg

    def _obj(self):
        return 'fundValueTaskLst'


if __name__ == '__main__':
        task = FundValueLstTask('task_004')

        task.excute()