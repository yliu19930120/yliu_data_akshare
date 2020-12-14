import fund_task
from dao import Dao

if __name__ == '__main__':

    fund_task.get_fund()

    dao = Dao("crawler", "fund")

    r = dao.findOne()

    print(r)