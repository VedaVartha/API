from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item["id"] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        item.update(request.json)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        data.remove(item)
        return jsonify({"message": "Item deleted"})
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


#Checking end points
#Run python scriptname.py in terminal to check get API