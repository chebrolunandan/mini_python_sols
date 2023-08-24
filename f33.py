import pymongo
MCob = pymongo.MongoClient('localhost',27017)
mydb = MCob["klucsit1"]
mytable = mydb["customers"]
myquery = {"cgpa": {"$gt":2}}
row = mytable.find(myquery)
for i in row:
    print(i)
