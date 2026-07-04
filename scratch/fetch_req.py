import requests
import json
import csv

url = 'https://api.cellphones.com.vn/v3/product/cate?cate=1217&sort=view&price=20000000~25000000&size=50'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/json'
}
res = requests.get(url, headers=headers)
print("Status:", res.status_code)
if res.status_code == 200:
    print("Success V3 REST")
else:
    print(res.text[:200])
