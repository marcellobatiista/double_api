from flask import Flask, request, jsonify
from double import DoubleAPI

app = Flask(__name__)
app.secret_key = '#$%^&*()xdrctfvygbuhnjimk,ol./;p0-='


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    double = DoubleAPI(username, password)

    if str(double.online).find('error') != -1:
        return jsonify(double.online), 401
    else:
        return jsonify({'access_token': double.s.headers['Authorization'].split()[1]})


@app.route('/me', methods=['GET'])
def get_me():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    print(api_login)
    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_me())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/wallet', methods=['GET'])
def get_wallet():
    access_token = request.headers.get('Authorization')
    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_wallet())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/xp', methods=['GET'])
def get_xp():
    access_token = request.headers.get('Authorization')
    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_xp())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/recent', methods=['GET'])
def get_recent():
    access_token = request.headers.get('Authorization')
    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_recent())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/current', methods=['GET'])
def get_current():
    access_token = request.headers.get('Authorization')
    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_current())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/bet', methods=['POST'])
def place_bet():
    access_token = request.headers.get('Authorization')
    if access_token:
        data = request.get_json()
        amount = data.get('amount')
        color = data.get('color')
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.bet(amount, color))
    else:
        return jsonify({'error': 'No access token provided'}), 401


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
