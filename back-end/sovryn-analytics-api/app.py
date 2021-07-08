from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/get_all_swap', methods=['GET'])
@cross_origin()
def get_all_swap():
    return jsonify({
        'NAME' : 'AKBAR',
        'IDRIA' : 'OJKE'
    })


if __name__ == '__main__':
    app.run()