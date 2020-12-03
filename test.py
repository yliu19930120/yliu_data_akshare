import fund_op
from dao import Dao

if __name__ == '__main__':

    fund_op.get_fund()

    dao = Dao("crawler", "fund")

    r = dao.findOne()

    print(r)