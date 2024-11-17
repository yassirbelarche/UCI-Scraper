from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from data_transformation import jsondata

uri = "mongodb+srv://yassirbelarche:cluster0Yas2$@cluster0.od39t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Replace <database> and <collection> with your database and collection names
db = client['Scraped_data']  # Replace 'my_database' with your database name
collection = db['UCI_data']  # Replace 'my_collection' with your collection name

# Insert the data
result = collection.insert_many(jsondata)
print(f"Data inserted with ID: {result.inserted_id}")

# Retrieve and display data
for doc in collection.find():
    print(doc)


