from bson import ObjectId
from flask import Flask, jsonify, request
# import pandas as pd
from pymongo import MongoClient
import re

app = Flask(__name__)
mongo_url='mongodb+srv://janhavipal:jaan2405@cluster0.s5pfi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(mongo_url)
db = client['janhavi']  # Replace with your database name
collection = db['medicine_sku']      # Replace with your collection name

# <<<<<<< HEAD

def serialize_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, dict):
        return {k: serialize_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize_objectid(item) for item in obj]
    return obj

@app.route('/api/v1/medicines', methods=['GET', 'POST'])
def manage_medicines():
    if request.method == 'GET':
        filter_value = request.args.get('name')
        print(f"Name filter value: {filter_value}")  # Debug log
        if filter_value:
            # Use a case-insensitive regex to filter by name
            regex = re.compile(filter_value, re.IGNORECASE)
            filtered_data = list(collection.find({'name': regex}))
            print(f"Filtered data: {filtered_data}")  # Debug log
            if not filtered_data:
                return jsonify({"error": "No medicines found with the given name"}), 404
            return jsonify(serialize_objectid(filtered_data))
        # Return the first 10 documents if no filter is applied
        data = list(collection.find().limit(10))
        data=serialize_objectid(data)
        return jsonify(serialize_objectid(data))
    elif request.method == 'POST':
        new_data = request.get_json()
        print(f"New data received: {new_data}")  # Debug log
        # Insert the new document into the collection
        result = collection.insert_one(new_data)
        result=serialize_objectid(result)
        return jsonify({"message": "Data received", "inserted_id": str(result.inserted_id)}), 201


@app.route('/api/v1/medicines/<id>', methods=['GET'])
def search_by_id(id):
    try:
        # Attempt to convert the ID to ObjectId
        object_id = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ID format: {str(e)}"}), 400

    # Query the database
    result = collection.find_one({"_id": object_id})

    if not result:
        return jsonify({"error": "No document found with the given ID"}), 404

    # Convert the ObjectId to string for JSON serialization
    result["_id"] = str(result["_id"])
    return jsonify(result), 200

    return jsonify(serialize_objectid(medicine))




@app.route('/api/v1/medicines/usage', methods=['GET'])
def search_by_usage():
    usage_query = request.args.get('usage')
    if not usage_query:
        return jsonify({"error": "Usage query parameter is required"}), 400

    # Use a case-insensitive regex to filter by usage
    regex = re.compile(usage_query, re.IGNORECASE)
    filtered_data = list(collection.find({'usage1': regex}))
    if not filtered_data:
        return jsonify({"error": "No medicines found for the given usage"}), 404

    filtered_data=serialize_objectid(filtered_data)
    return jsonify(filtered_data)


@app.route('/api/v1/medicines/component', methods=['GET'])
def search_by_component():
    component_query = request.args.get('component')
    if not component_query:
        return jsonify({"error": "Component query parameter is required"}), 400
    components = [comp.strip() for comp in component_query.split(',')]

    # Create regex patterns for each component
    # regex_patterns = [re.compile(comp, re.IGNORECASE) for comp in components]
    # components = [comp.strip() for comp in component_query.split(',')]

    # # Filter medicines based on composition1 or composition2
    # filtered_data = list(collection.find({
    #     '$or': [
    #         {'composition1': {'$regex': components, '$options': 'i'}}for comp in components]+[
    #         {'composition2': {'$regex': components, '$options': 'i'}}for comp in components
    #     ]
    # }))

    # Create the $or conditions for each component individually
    filter_conditions = []
    for comp in components:
        filter_conditions.append(
            {'composition1': {'$regex': comp, '$options': 'i'}}
        )
        filter_conditions.append(
            {'composition2': {'$regex': comp, '$options': 'i'}}
        )

    # Filter medicines based on the conditions
    filtered_data = list(collection.find({'$or': filter_conditions}))

    if not filtered_data:
        return jsonify({"error": "No medicines found for the given component"}), 404

    # Serialize ObjectId fields to strings
    filtered_data = serialize_objectid(filtered_data)

    return jsonify(filtered_data)




# @app.route('/api/v1/medicines/component', methods=['GET'])
# def search_by_component():
#     component_query = request.args.get('component')
#     if not component_query:
#         return jsonify({"error": "Component query parameter is required"}), 400
#     components = [comp.strip() for comp in component_query.split(',')]

#     # Create regex patterns for each component
#     regex_patterns = [re.compile(comp, re.IGNORECASE) for comp in components]

#     # Filter medicines based on composition1 or composition2
#     filtered_data = list(collection.find({
#         '$or': [
#             {'composition1': {'$in': regex_patterns}},
#             {'composition2': {'$in': regex_patterns}}
#         ]
#     }))
#     if not filtered_data:
#         return jsonify({"error": "No medicines found for the given component"}), 404
#     return jsonify(filtered_data)
from bson import ObjectId

def convert_objectid(data):
    if isinstance(data, list):
        return [convert_objectid(item) for item in data]
    elif isinstance(data, dict):
        return {k: convert_objectid(v) for k, v in data.items()}
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data


if __name__ == '__main__':
    app.run(debug=True)
