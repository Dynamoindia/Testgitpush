import pymongo
client = pymongo.MongoClient("mongodb+srv://Shivank10:Shivank1234@cluster0.bevdy9e.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "Shivank",
    "email": "ershivank95@gmail.com",
    "surname": "Singh"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)