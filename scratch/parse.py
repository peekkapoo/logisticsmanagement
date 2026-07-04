import re
import csv
import urllib.request
import json

try:
    req = urllib.request.Request(
        'https://api.cellphones.com.vn/v2/graphql',
        data=b'{"query":"query { products(filter: {category: {eq: 1217}, price: {from: 20000000, to: 25000000}}, size: 50) { id name price special_price } }"}',
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'},
        method='POST'
    )
    res = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(res)
    products = data.get('data', {}).get('products', [])
    print(f"GraphQL returned {len(products)} products")
except Exception as e:
    print(f"GraphQL Error: {e}")

try:
    text = open('d:/LogManagement/nuxt_data.txt', encoding='utf-8').read()
    # Looking for object-like string that has name:"...", ..., price:..., ..., special_price:...
    # Usually in nuxt it's very minified so we might just look for name:"Laptop...
    names = re.findall(r'name:"(Laptop.*?)"', text)
    print(f"Found {len(names)} names with 'Laptop' in nuxt")
except Exception as e:
    print(f"NUXT Error: {e}")
