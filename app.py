from flask import Flask, jsonify
from services.jsonplaceholder import get_posts

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def posts():
    result = get_posts()
    return jsonify(result), result['status_code']

if __name__ == '__main__':
    app.run(debug=True)