from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/swap", methods=["POST"])
def swap_face():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']

    # Save the uploaded image temporarily
    temp_path = "uploads"
    os.makedirs(temp_path, exist_ok=True)
    save_path = os.path.join(temp_path, image_file.filename)
    image_file.save(save_path)

    # TODO: Integrate AI face swapping logic here and return result

    return jsonify({"message": f"Image received: {image_file.filename}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
