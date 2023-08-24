import pymongo
MCob = pymongo.MongoClient('localhost',27017)
mydb = MCob["klucsit1"]
mytable = mydb["customers"]
myquery = {"cgpa": {"$lt":10}}
row = mytable.find(myquery)
for i in row:
    print(i)
