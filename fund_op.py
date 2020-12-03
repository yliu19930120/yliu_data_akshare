import akshare as ak
from datetime import datetime
from log_utils import log_utils
from dao import Dao
import pytz

log = log_utils.get_logger("fund_op")

def get_fund() -> object:
    log.info("获取基金的信息")
    fund_em_fund_name_df = ak.fund_em_fund_name()
    dao = Dao("crawler", "fund")
    dao.delete_many({})
    fund_em_fund_name_df["createTime"] = pytz.timezone('Asia/Shanghai').localize(datetime.now())
    fund_em_fund_name_df.rename(
    columns={"基金简称": "name", "基金类型": "fundType", "拼音全称": "fullPinyin", "基金代码": "code", "拼音缩写": "pinyin"}, inplace=True)
    records = fund_em_fund_name_df.to_dict(orient='records')
    dao.insert_many(records)

    log.info("基金信息获取完毕 共计 %s 条",len(records))

def get_lastest_fund_value() -> object:
    log.info("获取最新的基金净值")
    fund_em_open_fund_daily_df = ak.fund_em_open_fund_daily()
    # ['基金代码', '基金简称', '2020-11-30-单位净值', '2020-11-30-累计净值', '2020-11-27-单位净值', '2020-11-27-累计净值', '日增长值', '日增长率', '申购状态',
    #  '赎回状态', '手续费']
    print(fund_em_open_fund_daily_df.columns.values.tolist())
    # dao.insert_many(records)