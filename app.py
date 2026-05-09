from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["items"]

@app.route('/')
def home():
    return "Flask App Running"

@app.route('/submittodoitem', methods=['POST'])
def submit():
    item = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }
    collection.insert_one(item)
    return "Item stored successfully"

if __name__ == '__main__':
    app.run(debug=True)