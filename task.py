
import requests
from log_utils import log_utils

schedule_server = "http://scheduleserver:10003/yliu/"
url = schedule_server + "task/"
log = log_utils.get_logger("task")
succ = "2"
fail = "3"


class Task(object):

    def __init__(self, task_id, log_id):
        self.task_id = task_id
        self.log_id = log_id


    def excute(self):
        return '成功'

    def run(self):
        try:
            msg = self.excute()
            log.info("成功")
            self.callback(succ,msg)
        except Exception as e:
            log.info("失败 %s ",e)
            self.callback(fail,msg)



    def callback(self, status, msg):
        requests.post(url + "callback", data={"taskId": self.task_id, "logId": self.log_id, "status":status,"msg": msg})