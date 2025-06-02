from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://rev:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.route('/')
def home():
    collection.insert_one({"name": "Sahil 🚀"})
    user = collection.find_one()
    return f"User in MongoDB: {user['name']}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


