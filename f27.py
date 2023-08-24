import pymongo
mongoclient = pymongo.MongoClient('localhost',27017)
mydb = mongoclient["klucsit1"]
mytable = mydb["customers"]
mydict = {"custid":9004,"cname":"Nandan"}
mytable.insert_one(mydict)
mydict = {"custid":30543,"cname":"sid","address":"bezawada"}
mytable.insert_one(mydict)
mytable.drop()
for i in mytable.find():
    print(i)