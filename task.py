
import requests
from log_utils import log_utils
import _thread

schedule_server = "http://scheduleserver:10003/yliu/"
url = schedule_server + "task/"
log = log_utils.get_logger("task")
OK = {"code":200,"msg":"OK"}

class Task(object):

    def __init__(self, task_id):
        self.task_id = task_id


    def excute(self):
        return '成功'
    #task的名称标记
    def _obj(self):
        return 'task'

    def run(self):
        self.running()
        try:
            msg = self.excute()
            log.info("成功")
            self.succ(msg)
        except Exception as e:
            print(e)
            log.info("失败 %s ",e)
        finally:
            self.freed()




    def running(self):
        requests.post(url+"running", data= {"id":self.task_id})

    def freed(self):
        requests.post(url+"freed", data= {"id":self.task_id})

    def failed(self,msg):
        requests.post(url + "failed", data={"taskId": self.task_id,"msg":msg,"objectName":self._obj()})

    def succ(self, msg):
        requests.post(url + "success", data={"taskId": self.task_id, "msg": msg, "objectName": self._obj()})