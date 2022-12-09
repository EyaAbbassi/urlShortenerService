from flask import jsonify, request
import validators
from app import app
from app.util import Random_generator
from app.repository import Url_repository

shortning_tools = Random_generator.Random_generator()
url_tools = Url_repository.Url_repository()


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

    if url_tools.is_exist_key(key):
        return jsonify({
            'status': '400',
            'message': 'Please try another key!'
        }), 400

    if url_tools.is_exist_url(original_url) and not key:
        return jsonify(url_tools.get_short_URL(original_url))

    if not key:
        key = shortning_tools.generate_random_key()

    url_tools.save_url(original_url, key)
    return jsonify(url_tools.get_short_URL(original_url))


@app.route('/decode')
def decode_url():
    short_url = request.json['short_url']
    if not short_url:
        return jsonify({
            'status': '400',
            'message': 'The URL is required!'
        }), 400
    is_valid = url_tools.is_valid_short_url(short_url)
    if not is_valid:
        return jsonify({
            'status': '400',
            'message': 'The URL is not valid!'
        }), 400

    key = url_tools.get_key(short_url)

    long_url = url_tools.get_long_URL(key)
    if not long_url:
        return jsonify({'status': '404', 'message': 'The URL not found!'}), 404
    else:
        return jsonify(long_url)
