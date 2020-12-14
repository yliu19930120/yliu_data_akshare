
from flask import Flask
import _thread

from fund_task import FundTask
from log_utils import log_utils

OK = {"code":200,"msg":"OK"}

app = Flask(__name__)
log = log_utils.get_logger("app")

@app.route('/fund', methods=['GET'])
def getfund():
    fund_task = FundTask()
    _thread.start_new_thread(fund_task.get_fund, ())

if __name__ == '__main__':
    app.run(port=10002)