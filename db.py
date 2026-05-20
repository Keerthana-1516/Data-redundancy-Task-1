from pymongo import MongoClient

client = MongoClient("mongodb+srv://Keerthana:Chinny123@cluster0.nj7gdx4.mongodb.net/?appName=Cluster0")

db = client["task1_db"]      # NEW DATABASE
collection = db["users"]     # COLLECTION

collection.insert_one({"name": "keerthana", "age": 22})

print("Inserted successfully")