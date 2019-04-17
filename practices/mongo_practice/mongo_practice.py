from pymongo import MongoClient


class MongoTest:
    connect=MongoClient(host='127.0.0.1',port=27017)
    db=connect.mydb
    test_users=db.test_users
    users = [
        {
            'name': 'guygubaby',
            'age': 22
        },
        {
            'name': 'mistletoe',
            'age': 23
        }
    ]

    def test_insert_save_data(self):
        res=self.test_users.insert_many(self.users)
        print(res)

    def test_find(self,name='guygubaby'):
        user=self.test_users.find().limit(2)
        for i in user:
            print(i)

    def test_update(self,old_name,new_name):
        self.test_users.update_one({'name':old_name},{'$set':{'name':new_name}})

    def test_delete(self,name):
        self.test_users.delete_one({'name':name})


if __name__ == '__main__':
    mongo_test=MongoTest()
    # mongo_test.test_insert_save_data()
    # mongo_test.test_find()
    # mongo_test.test_update('guygubaby','yjb')
    # mongo_test.test_find('yjb')
    mongo_test.test_delete('yjb')
    mongo_test.test_find('yjb')
