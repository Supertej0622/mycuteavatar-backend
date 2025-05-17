import os
import replicate
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["https://mycuteavatar.com"])

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)

@app.route("/swap", methods=["POST"])
def swap_faces():
    if 'your_image' not in request.files or 'target_image' not in request.files:
        return jsonify({"error": "Images not uploaded"}), 400

    your_image = request.files['your_image']
    target_image = request.files['target_image']

   output = replicate_client.run(
    "cdingram/face-swap",
    input={"source_image": your_image, "target_image": target_image}
)


    return jsonify({"image": output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
