from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})