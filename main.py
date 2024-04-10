import requests

headers = {'user-x-pswd': 'marcello@36259200'}
payload = {'username': 'marcellobatiista@gmail.com', 'password': '36259200M@b@'}

r = requests.post('http://127.0.0.1:5010/login', json=payload, headers=headers)
if r.status_code == 200:
    headers.update({'Authorization': r.json().get('access_token')})

r = requests.get('http://127.0.0.1:5010/me', headers=headers)
print(r.json())

