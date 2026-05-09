from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["todoItems"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    data = request.json

    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }

    collection.insert_one(item)

    return jsonify({"message": "Item Added"})


if __name__ == '__main__':
    app.run(debug=True)