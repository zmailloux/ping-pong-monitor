import requests
res = requests.post('http://34.69.249.145/api/test', json={"mytext":"lalala"})
if res.ok:
    print(res.json())