import pymongo
mongoclient = pymongo.MongoClient('localhost',27017)
mydb = mongoclient["klucsit1"]
mytable = mydb["customers"]
myquery ={"name":{"$eq":"sid"}}
row = mytable.find(myquery)
for i in mytable.find():
    print(i)