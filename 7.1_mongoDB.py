# mongoDB 操作
import pymongo
client = pymongo.MongoClient('localhost', 27017)
mydb = client['test']   #  新建 test 数据库
test = mydb['test']     # 新建 test 数据集合

test.insert_one({'name':'Jan','sex':'男','grade':89})
