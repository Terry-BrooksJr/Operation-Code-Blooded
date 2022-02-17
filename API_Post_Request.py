
import requests
import json 
import csv

FilePath = '/Users/terrybrooksjr/Documents/GitHub/Operation-Code-Blooded/ZenDeskTickets/Python_API_Post_Tkt_1255/API_Import.json'
url = 'https://api.us.flatfile.io/workspace/fe1d96a6-0a41-4f7f-8c52-c8bd6b3089b5/sheet/117233/'
headers = {'X-Api-Key': 'FF00UL3BZLO43DPTUYUAJ8GB2QK6Q82N54QV30EW+PJ0t0F32PgvcyGjl7JjW0wqSUcrYpfRWvuRJszKb',
           'Accept': 'application/json', 'Content-Type': 'application/json'}
body:{ur}
r = requests.post(url, data=open(FilePath, 'rb'), headers=headers)
print(r.status_code)


headers = {'Authorization': ‘(some auth code)’, 'Accept': 'application/json', 'Content-Type': 'application/json'}
r = requests.post(url, data=open('example.json', 'rb'), headers=headers)
