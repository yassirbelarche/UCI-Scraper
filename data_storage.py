from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from data_transformation import csv_to_dicts

uri = "mongodb+srv://yassirbelarche:cluster0Yas2$@cluster0.od39t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)

# Replace <database> and <collection> with your database and collection names
db = client['Scraped_data']  # Replace 'Scraped_data' with your database name
collection = db['UCI_data']  # Replace 'UCI_data' with your collection name

data_dicts = csv_to_dicts()

# Insert the data into MongoDB
try:
    result = collection.insert_many(data_dicts)
    print(f"Data inserted with IDs: {result.inserted_ids}")
except Exception as e:
    print("Error inserting data:", e)

# Retrieve and display data
for doc in collection.find():
    print(doc)
