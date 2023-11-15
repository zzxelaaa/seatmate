from flask import Flask, jsonify, request

app = Flask(__name__)

hearts = [
    {"heart_id": "0", "date": "01/01/2021", "heart_rate": "111bpm"},
    {"heart_id": "1", "date": "02/02/2022", "heart_rate": "222bpm"},
]


@app.route("/post", methods=["POST"])
def add_heart():
    new_heart = request.get_json()
    hearts.append(new_heart)
    return jsonify({}), 201


@app.route("/get", methods=["GET"])
def get_hearts():
    return jsonify({"hearts": hearts})


@app.route("/get/<string:heart_id>", methods=["GET"])
def get_heart(heart_id):
    heart = next((item for item in hearts if item["heart_id"] == heart_id), None)
    if heart:
        return jsonify({"heart": heart})
    else:
        return jsonify({}), 404


@app.route("/put/<string:heart_id>", methods=["PUT"])
def update_heart(heart_id):
    heart = next((item for item in hearts if item["heart_id"] == heart_id), None)
    if heart:
        updated_heart = request.get_json()
        heart.update(updated_heart)
        return jsonify({})
    else:
        return jsonify({}), 404


@app.route("/delete/<string:heart_id>", methods=["DELETE"])
def delete_heart(heart_id):
    global hearts
    hearts = [item for item in hearts if item["heart_id"] != heart_id]
    return jsonify({})


if __name__ == "__main__":
    app.run()
