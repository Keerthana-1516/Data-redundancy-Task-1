from db import collection

def is_duplicate(data):
    return collection.find_one({
        "name": data["name"],
        "age": data["age"]
    }) is not None


def add_data(data):
    if is_duplicate(data):
        print("❌ Duplicate data found")
    else:
        collection.insert_one(data)
        print("Inserted successfully")


# CLEAN TEST RUN
collection.delete_many({})   

add_data({"name": "keerthana", "age": 22})
add_data({"name": "chinny", "age": 21})
add_data({"name": "chinny", "age": 20})
add_data({"name": "keerthana", "age": 22})  # duplicate test