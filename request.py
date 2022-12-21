import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={
"imageBase64": "Base64EnkodiranaSlikaOsmice"
})
print(r.json())