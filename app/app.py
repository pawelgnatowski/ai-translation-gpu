import os
from flask import Flask, request, jsonify
from translate import HuggingFaceTranslator
from config import *

app = Flask(__name__)
translator = HuggingFaceTranslator(MODEL_PATH,True) # True flag to use GPU => load tensorflow model to GPU, False to use CPU

app.config["DEBUG"] = True


@app.route('/', methods=["GET"])
def is_running():
    return "ML translate service is up and running."

@app.route('/get_routes', methods = ["GET"])
def get_available_language_route():
    """Shows a list of available language pairs

    Returns:
        dict: A list of available language pairs
    EXAMPLES:
        http://localhost:5030/get_routes
        returns:
        {
  "output": [
    [
      "lt", 
      "pl"
    ], 
    [
      "ar", 
      "pl"
    ]
http://localhost:5030/get_routes?lang=pl
    {
  "output": [
    [
      "pl", <= trnaslation from Polish
      "en" <= translation to English
    ]
  ]
}
}
    """    
    requestedLanguageRoute = request.args.get('lang')
    all_available_models = translator.get_downloaded_language_models()
    # return all if no specific language is requested
    # return single language => e.g. ?lang=lt
    language_routes = [language for language in all_available_models if requestedLanguageRoute is None or requestedLanguageRoute == language[0]]
    return jsonify({"output":language_routes})


@app.route('/translate', methods=["POST"])
def get_prediction():
    source = request.json['from']
    target = request.json['to']
    text = request.json['text']
    translation = translator.translate(source, target, text)
    return jsonify({"output":translation})

app.run(host="0.0.0.0")