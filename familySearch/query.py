import requests
import os
import json

accessToken = "351eb513-bcb2-4109-9332-49806f4c1fa0-prod"


#response = requests.get('https://google.com')
url = 'https://familysearch.org'
PID = 'KWJR-6QD'
query = '/platform/tree/ancestry?person=' + PID
header={
    "GET" : query,
    "Accept" : "application/x-fs-v1+json",
    "Authorization" : accessToken
    }
response = requests.request("GET", url, headers=header)
print("---------------")
print (response)
print("---------------")
with open("familySearch//response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

'''
textfile = 'KimballPIDQuery.txt'
fullPath = os.getcwd() + "\\" + textfile
print("Begin writing text to ", fullPath, "...")
f = open(fullPath, 'w')
f.write(response.text)
print("Wrote json text to ", textfile)

#GET /platform/tree/ancestry?person=P1sin-01
#Accept: application/x-fs-v1+json
#Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
'''