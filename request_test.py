import requests

req = requests.post("http://127.0.0.1:8000/get_form", json={ "field_0": "email" })

print(req.content)
req = requests.post("http://127.0.0.1:8000/get_form", json={"field_0": "email", "field_0123": "email"})
print(req.content)

req = requests.post("http://127.0.0.1:8000/get_form", json={"First name": "text", "Second name": "text", "email": "email"})
print(req.content)
req = requests.post("http://127.0.0.1:8000/get_form", json={"First name": "text", "Second name": "text"})
print(req.content)
req = requests.post("http://127.0.0.1:8000/get_form", json={"First name": "text", "Second name": "texttt"})
print(req.content)