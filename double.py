import json
import requests


class DoubleAPI:
    def __init__(self, username: str = '', password: str = ''):
        self.s = requests.Session()
        self.username = username
        self.password = password
        self.online = self.__login()

    def __str__(self):
        return str(self.online)

    def __login(self):
        if not self.username or not self.password:
            return {'error': 'username or password not provided'}

        response = self.s.put(
            'https://blaze1.space/api/auth/password?analyticSessionID=1711825505194',
            json={
                "username": self.username,
                "password": self.password
            })
        if response.status_code == 200:
            self.s.headers.update(
                {
                    'Authorization': f'Bearer {response.json().get("access_token")}'
                })
            return {
                'username': self.get_me()['username'],
                'balance': self.get_wallet()['balance']
            }
        return response.text

    def get_me(self):
        response = self.s.get('https://blaze1.space/api/users/me')
        if response.status_code == 200:
            return response.json()
        return json.loads(response.text)

    def get_wallet(self):
        response = self.s.get('https://blaze1.space/api/wallets')
        if response.status_code == 200:
            return response.json()[-1]
        return json.loads(response.text)

    def get_xp(self):
        response = self.s.get('https://blaze1.space/api/users/me/xp')
        if response.status_code == 200:
            return response.json()
        return json.loads(response.text)

    def get_recent(self):
        response = self.s.get('https://blaze1.space/api/roulette_games/recent')
        if response.status_code == 200:
            return response.json()
        return json.loads(response.text)

    def get_current(self, tryout=30):
        response = self.s.get('https://blaze1.space/api/roulette_games/current')
        if tryout <= 0:
            return json.loads(response.text)
        while response.status_code != 200:
            self.get_current(tryout - 1)
        return response.json()

    def bet(self, amount: float, color: int):
        wallet = self.get_wallet()
        response = self.s.post(
            'https://blaze1.space/api/roulette_bets',
            json={
                "amount": amount,
                "currency_type": wallet.get('currency_type'),
                "color": color,
                "free_bet": False,
                "wallet_id": wallet.get('id')
            })
        if response.status_code == 200:
            return response.json()
        return json.loads(response.text)

    def bet_win(self, amount: float, color: int):
        _b = self.bet(amount, color)
        _r = self.wait_result()
        return {
            'bet': _b,
            'result': _r
        }

    def wait_result(self):
        gc = self.get_current()
        while gc['status'] != 'rolling':
            gc = self.get_current()
        return gc


if __name__ == '__main__':
    double = DoubleAPI()
    print(double)
