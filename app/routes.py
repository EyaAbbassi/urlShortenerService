from flask import jsonify, request
import validators
from app import app
from app.util import RandomGenerator, urlRepository

shortning_tools = RandomGenerator.RandomGenerator()
url_tools = urlRepository.Repository()


@app.route('/encode', methods=['POST'])
def encode_url():
    original_url = request.json["long_url"]
    key = request.json['custom_id']

    if not original_url:
        return jsonify({
            'status': '400',
            'message': 'The URL is required!'
        }), 400

    if not validators.url(original_url):
        return jsonify({
            'status': '400',
            'message': 'Please enter a valid URL!'
        }), 400

    if not key:
        key = shortning_tools.generate_random_key()

    url_tools.save_url(original_url, key)
    return jsonify(url_tools.get_short_URL(original_url))
