from pymongo import MongoClient


if __name__ == '__main__':
    client=MongoClient('127.0.0.1',27017)
    woaidu_db=client.mydb.woaidu

    for i in woaidu_db.find().limit(10):
        print(i)