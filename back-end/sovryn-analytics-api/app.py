from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
from database.database import database

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/get_kpi_swap', methods=['GET'])
@cross_origin()
def get_kpi_swap():
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_the_largest_swap(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_the_largest_swap(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_the_largest_swap()
        return jsonify(_largest_swap)

@app.route('/api/get_swap_distribution', methods=['GET'])
@cross_origin()
def get_swap_distribution() :
    _d = database()
    _result = {}
    _r = _d.get_rbtc_doc()
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _r1 = _d.get_rbtc_doc(_args["from_date"], _args["to_date"])
            _r2 = _d.get_rbtc_rusdt(_args["from_date"], _args["to_date"])
            _r3 = _d.get_rbtc_bpro(_args["from_date"], _args["to_date"])
            _r4 = _d.get_rbtc_sov(_args["from_date"], _args["to_date"])
            return jsonify([_r1, _r2, _r3, _r4])
        else :
            _r1 = _d.get_rbtc_doc(_args["from_date"], _args["to_date"], _args["wallet"])
            _r2 = _d.get_rbtc_rusdt(_args["from_date"], _args["to_date"], _args["wallet"])
            _r3 = _d.get_rbtc_bpro(_args["from_date"], _args["to_date"], _args["wallet"])
            _r4 = _d.get_rbtc_sov(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify([_r1, _r2, _r3, _r4])
    else :
        _r1 = _d.get_rbtc_doc()
        _r2 = _d.get_rbtc_rusdt()
        _r3 = _d.get_rbtc_bpro()
        _r4 = _d.get_rbtc_sov()
        return jsonify([_r1, _r2, _r3, _r4])

@app.route('/api/get_total_swap', methods=['GET'])
@cross_origin()
def get_total_swap() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_total_swap(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_total_swap(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_total_swap()
        return jsonify(_largest_swap)

@app.route('/api/get_swap_month', methods=['GET'])
@cross_origin()
def get_swap_month() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_swap_month(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_swap_month(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_swap_month()
        return jsonify(_largest_swap)

@app.route('/api/get_swap_user', methods=['GET'])
@cross_origin()
def get_swap_user() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_swap_user(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_swap_user(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_swap_user()
        return jsonify(_largest_swap)

@app.route('/api/get_swap_user_month', methods=['GET'])
@cross_origin()
def get_swap_user_month() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_swap_user_month(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_swap_user_month(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_swap_user_month()
        return jsonify(_largest_swap)

@app.route('/api/get_spent_gas_date', methods=['GET'])
@cross_origin()
def get_spent_gas_date() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_spent_gas_date(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_spent_gas_date(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_spent_gas_date()
        return jsonify(_largest_swap)

@app.route('/api/get_spent_gas_month', methods=['GET'])
@cross_origin()
def get_spent_gas_month() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_spent_gas_month(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_spent_gas_month(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_spent_gas_month()
        return jsonify(_largest_swap)

@app.route('/api/top_trader', methods=['GET'])
@cross_origin()
def top_trader() :
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.top_trader(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.top_trader(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.top_trader()
        return jsonify(_largest_swap)

@app.route('/api/get_kpi_lending', methods=['GET'])
@cross_origin()
def get_kpi_lending():
    _d = database()
    _result = {}
    if request.args :
        _args = request.args
        if "wallet" not in _args :
            _largest_swap = _d.get_kpi_lending(_args["from_date"], _args["to_date"])
            return jsonify(_largest_swap)
        else :
            _largest_swap = _d.get_kpi_lending(_args["from_date"], _args["to_date"], _args["wallet"])
            return jsonify(_largest_swap)
    else :
        _largest_swap = _d.get_kpi_lending()
        return jsonify(_largest_swap)



if __name__ == '__main__':
    app.run()