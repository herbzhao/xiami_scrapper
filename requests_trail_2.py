import requests

data = [
  ('task', 'something new'),
]

response = requests.post('http://localhost:5000/todos', data=data)
response = requests.get('http://localhost:5000/todos').json()
print(response)
