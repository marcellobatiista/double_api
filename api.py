import json
import os

from flask import Flask, request, jsonify
from double import DoubleAPI

app = Flask(__name__)
app.secret_key = '#$%^&*()xdrctfvygbuhnjimk,ol./;p0-='


def x_auth(_api_login):
    with open('users.json', 'r') as _f:
        users = json.loads(_f.read())
    if users:
        return users.get(_api_login, None)


@app.route('/login', methods=['POST'])
def login():
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

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
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_me())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/wallet', methods=['GET'])
def get_wallet():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_wallet())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/xp', methods=['GET'])
def get_xp():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_xp())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/recent', methods=['GET'])
def get_recent():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_recent())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/current', methods=['GET'])
def get_current():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.get_current())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/bet', methods=['POST'])
def place_bet():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        data = request.get_json()
        amount = data.get('amount')
        color = data.get('color')
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.bet(amount, color))
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/result', methods=['GET'])
def wait_result():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.wait_result())
    else:
        return jsonify({'error': 'No access token provided'}), 401


@app.route('/bet_result', methods=['POST'])
def place_bet_win():
    access_token = request.headers.get('Authorization')
    api_login = request.headers.get('user-x-pswd')
    if not x_auth(api_login):
        return jsonify({'error': 'Unauthorized'}), 401

    if access_token:
        data = request.get_json()
        amount = data.get('amount')
        color = data.get('color')
        double = DoubleAPI()
        double.s.headers.update({'Authorization': f'Bearer {access_token}'})
        return jsonify(double.bet_win(amount, color))
    else:
        return jsonify({'error': 'No access token provided'}), 401


if __name__ == '__main__':
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as f:
            f.write('{}')

    app.run(debug=False, port=5010)
