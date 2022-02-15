
import requests
import json 
import csv

FilePath = '/Users/terrybrooksjr/Documents/GitHub/Operation-Code-Blooded/ZenDeskTickets/Python_API_Post_Tkt_1255/API_Import.json'
url = 'https://api.us.flatfile.io/workspace/fe1d96a6-0a41-4f7f-8c52-c8bd6b3089b5/sheet/117233/'
headers = {'Content-Type': 'application/json', 'X-Api-Key': 'X-Api-Key}
body:{ur}
r = requests.post(url, data=open(FilePath, 'rb'), headers=headers)
print(r.status_code)
