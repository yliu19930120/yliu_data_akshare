
from flask import Flask
from flask import request
import const

import _thread

from fund_task import FundTask
from log_utils import log_utils


app = Flask(__name__)
log = log_utils.get_logger("app")

@app.route('/fund', methods=['GET'])
def getfund():
    task_id = request.args.get("task_id")
    fund_task = FundTask(task_id)
    _thread.start_new_thread(fund_task.run, ())
    return const.OK


if __name__ == '__main__':
    app.run(port=10002)