from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["todo_database"]

collection = db["todo_items"]

try:
    client.admin.command("ping")
    print("MongoDB connected successfully")
except Exception as e:
    print("MongoDb connection error :",e)


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        data = request.get_json(silent=True) or request.form

        itemName = data.get("itemName")
        itemDescription = data.get("itemDescription")

        if not itemName or not itemDescription:
            return jsonify({
                "error": "Both fields are required"
            }), 400

        todo = {
            "itemName": itemName,
            "itemDescription": itemDescription
        }

        collection.insert_one(todo)

        return jsonify({
            "message": "To-Do item saved successfully"
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

