
from flask import Flask
from flask import request
import const

import _thread

from fund_task import FundTask
from fund_value_his_task import FundValueHisTask
from fund_value_lst_task import FundValueLstTask
from log_utils import log_utils


app = Flask(__name__)
log = log_utils.get_logger("app")

@app.route('/fund', methods=['GET'])
def getfund():
    fund_task = FundTask(request.args.get("task_id"),request.args.get("log_id"))
    _thread.start_new_thread(fund_task.run, ())
    return const.OK


@app.route('/fundvaluehis', methods=['GET'])
def getfundValueHis():
    fund_task = FundValueHisTask(request.args.get("task_id"),request.args.get("log_id"))
    print(fund_task.log_id,fund_task.task_id)
    # _thread.start_new_thread(fund_task.run, ())
    return const.OK


@app.route('/fundvaluelst', methods=['GET'])
def getfundValueLst():
    fund_task = FundValueLstTask(request.args.get("task_id"),request.args.get("log_id"))
    _thread.start_new_thread(fund_task.run, ())
    return const.OK




if __name__ == '__main__':
    app.run(port=10002)