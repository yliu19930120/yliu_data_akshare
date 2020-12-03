
from flask import Flask
import _thread

import fund_op
from log_utils import log_utils

OK = {"code":200,"msg":"OK"}

app = Flask(__name__)
log = log_utils.get_logger("app")

@app.route('/fund', methods=['GET'])
def getfund():
    try:
        _thread.start_new_thread(fund_op.get_fund, ())
        log.info("成功")
    except Exception as e:
        print(e)
        return {"code":500,"msg":"失败 %s" % e}
    else:
        return OK

if __name__ == '__main__':
    app.run(port=10002)