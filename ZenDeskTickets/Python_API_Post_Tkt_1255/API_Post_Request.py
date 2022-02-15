
import requests
import json 
import csv

# """
# Function to convert a CSV to JSON
# """
# # Takes the file paths as arguments
csvFilePath = './ZenDeskTickets/Python_API_Post_Tkt_1255/API_Import.json'


# def make_json(csvFilePath, jsonFilePath):
#         jsonArray = []
#         #Converting to a Python JSON Array
#         with open(csvFilePath, encoding='utf-8') as CSV_File:
#             CSV_reader = csv.DictReader(CSV_File)
            
#             for row in CSV_reader:
#                 jsonArray.append(row)
#             print(jsonArray)
# #Variables

url = 'https: // api.us.flatfile.io/workspace/fe1d96a6-0a41-4f7f-8c52-c8bd6b3089b5/sheet/117233/data'
headers = {'Content-Type': 'application/json', 'X-Api-Key': 'FF00UL3BZLO43DPTUYUAJ8GB2QK6Q82N54QV30EW+PJ0t0F32PgvcyGjl7JjW0wqSUcrYpfRWvuRJszKb'}
r = requests.post(url, data=open('csvFilePath', 'rb'), headers=headers)
