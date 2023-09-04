from flask import Blueprint, request, jsonify, session
import requests

meme_bp = Blueprint('memes', __name__)

@meme_bp.route('/get_meme', methods=['GET'])
def get_meme():
    meme_api_url = "https://meme-api.com/gimme/1"
    response = requests.get(meme_api_url)

    if response.status_code == 200:
        meme_data = response.json()
        memes = meme_data.get("memes", [])
        
        if memes:
            meme = memes[0]  # Assuming you want the first meme from the list
            return jsonify({
                "postLink": meme.get("postLink", ""),
                "subreddit": meme.get("subreddit", ""),
                "title": meme.get("title", ""),
                "url": meme.get("url", ""),
                "nsfw": meme.get("nsfw", False),
                "spoiler": meme.get("spoiler", False),
                "author": meme.get("author", ""),
                "ups": meme.get("ups", 0),
                "preview": meme.get("preview", [])
            })
        else:
            return jsonify({"message": "No memes found in the response."}), 404
    else:
        return jsonify({"message": "Failed to fetch meme data."}), response.status_code

get_meme()