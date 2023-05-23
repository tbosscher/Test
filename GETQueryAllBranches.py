import requests
import json

url = "https://partner-api.avionte.com/authorize/token"

payload='grant_type=client_credentials&client_id=partner.api.axios&client_secret=I%242%2366wKrLpQ&scope=avionte.aero.compasintegrationservice'
headers = {
  'Ocp-Apim-Subscription-Key': '0db9068b8b41474a8566c1a1e5207857',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, headers=headers, data=payload)

print(response.json()['access_token'])
access_token = response.json()['access_token']


headers.update({'Authorization' : 'Bearer ' + access_token})

url = "https://partner-api.avionte.com/front-office/v1/branch"

response = requests.get(url, headers=headers)

#print(response.text)

with open("branches.json", "w") as outfile:
    outfile.write(response.text)