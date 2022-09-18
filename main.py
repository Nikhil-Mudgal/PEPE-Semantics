from flask import Flask, request, jsonify
import os
#import torch
#import faiss
#import transformers
import pepe_semantics
from pepe_semantics.inference import get_giphy_links

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """Takes a POST request with a key of \"text\" and the text to be classified."""
    data_dict = request.get_json()

    text = data_dict["text"]

    return jsonify({"result": f'GIPHY: {str(get_giphy_links(text, k = 5))}'})

@app.route("/")
def hello_world():
    #print(get_giphy_links("Hello world!", k = 5))
    #print(type(get_giphy_links("Hello world!", k = 5)))
    return str(get_giphy_links("Hello world!", k = 5))
    #return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))