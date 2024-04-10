import requests

r = requests.post('http://127.0.0.1:5000/login',
                  json={'username': 'marcellobatiista@gmail.com',
                        'password': '36259200M@b@'})
print(r.status_code)
token = r.json()
print(token)

r = requests.get('http://127.0.0.1:5000/me',
                 headers={'Authorization': token.get('access_token'),
                          'user-x-pswd': 'marcello@36259200'
                          })
print(r.status_code)
print(r.json())
