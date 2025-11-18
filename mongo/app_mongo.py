from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.sf_library

pipeline = [
    {"$group": {"_id": "$branch_name", "total_checkouts": {"$sum": "$total_checkouts"}}},
    {"$sort": {"total_checkouts": -1}},
    {"$limit": 5}
]
print("Top 5 branches by total checkouts:")
for stat in db.activities.aggregate(pipeline):
    print(f'Branch: {stat["_id"]}, Total Checkouts: {stat["total_checkouts"]}')

