from flask import Flask, jsonify, request
import pandas as pd
import re

app = Flask(__name__)

df = pd.read_csv(r"resource\medicine_names.csv")
print(df.head())

@app.route('/api/v1/medicines', methods=['GET', 'POST'])
def manage_medicines():
    if request.method == 'GET':
        filter_value = request.args.get('name')
        if filter_value:
            filtered_data = df[df['Name'].str.contains(filter_value, case=False)].to_dict(orient='records')
            return jsonify(filtered_data)
        return jsonify(df.head(10).to_dict(orient='records'))
    elif request.method == 'POST':
        new_data = request.get_json()
        # Example: Append to the data (in practice, save it to a database or file)
        return jsonify({"message": "Data received", "data": new_data}), 201

@app.route('/api/v1/medicines/<int:medicine_id>', methods=['GET'])
def get_medicine_by_id(medicine_id):
    
    filtered_data = df[df['id'] == medicine_id].to_dict(orient='records')
    if not filtered_data:
        return jsonify({"error": "Medicine not found"}), 404
    return jsonify(filtered_data)

@app.route('/api/v1/medicines/<string:medicine_name>', methods=['GET'])
def get_medicine_name(medicine_name):
    # Create a regex pattern to match names that start with the given query
    pattern = f"^{re.escape(medicine_name)}(?![a-zA-Z]).*"

    filtered_name= df[df['name'].str.contains(pattern, case=False, na=False,regex=True)].to_dict(orient='records')
    if not filtered_name:
        return jsonify({"error":"Medicine Not found"}),404
    return jsonify(filtered_name)

if __name__ == '__main__':
    app.run(debug=True)
