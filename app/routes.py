from flask import jsonify, request
import validators
from app import app
from app.util import RandomGenerator, urlRepository

shortning_tools = RandomGenerator.RandomGenerator()
url_tools = urlRepository.Repository()

@app.route('/encode', methods=['POST'])
def encode_url():
    original_url= request.json["long_url"]
    custom_id= request.json['custom_id'] 
    random_id= ""

    if not original_url:
        return jsonify({
            'status': 'error',
            'message': 'The URL is required!'
        }), 400 #bad request

    if not validators.url(original_url):
        return jsonify({
            'status': 'error',
            'message': 'Please enter a valid URL!'
        }), 400 #bad request

    if url_tools.is_exist_url(original_url):
        return jsonify(url_tools.get_short_URL(original_url))

    if not custom_id:
        random_id= shortning_tools.generate_random_key()   
    
    url_tools.save_url(original_url, random_id or custom_id)       
    return jsonify(url_tools.get_short_URL(original_url))
