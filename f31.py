import pymongo
MCob = pymongo.MongoClient('localhost',27017)
mydb = MCob["klucsit1"]
mytable = mydb["customers"]
for i in mytable.find():
    print(i)
