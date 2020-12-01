
from flask import Flask
from flask import request
import _thread

import fund_op
from log_utils import log_utils

OK = {"code":200,"msg":"OK"}
FAILED = {"code":500,"msg":"FAILED"}

app = Flask(__name__)
log = log_utils.get_logger("app")

@app.route('/fund', methods=['GET'])
def getfund():
    try:
        _thread.start_new_thread(fund_op.get_fund, ())
        log.info("成功")
    except Exception as e:
        print(e)
        return FAILED
    else:
        return OK

if __name__ == '__main__':
    app.run(port=10002)