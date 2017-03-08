from pymongo import MongoClient

client = MongoClient()
db = client.alibaba

# for n in range(30):
#     db.keywords.find_one_and_update({'done':{'$exists':True}},{'$unset':{"done":""}})

#如果field不存在，则从from转移到to
def transfer_record(from_collection,to_collection,field,num):
    for n in range(num):
        cursor = db[from_collection].find_one_and_delete({field:{'$exists':False}})
        db[to_collection].insert_one(cursor)

transfer_record('keywords','keywords_1','done',10000)
