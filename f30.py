import pymongo
MCob = pymongo.MongoClient('localhost',27017)
mydb = MCob["klucsit1"]
mytable = mydb["customers"]
mytable.drop()
mylist = [
    {"_id" : 1, "name": "John", "course": "CSE"},
    {"_id" : 2, "name": "Smith", "course": "AI"},
    {"_id" : 3, "name": "Ram"," course": "DATA SCIENCE"},
    {"_id" : 4, "name": "Ravi", "course": "CYBER SECURITY"},
    {"_id" : 5, "name": "Peter", "course": "IOT"},
    {"_id" : 6, "name": "Srinu", "cgpa": 8.9},
    {"_id" : 7, "name": "Krishna", "cgpa": 5.4},
    {"_id" : 8, "name": "Ravi", "cgpa": 7.2}
]
x = mytable.insert_many(mylist)
for i in mytable.find():
    print(i)
