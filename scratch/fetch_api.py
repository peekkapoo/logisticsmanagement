import urllib.request
import json
import csv

url = 'https://api.cellphones.com.vn/v3/product/cate?cate=1217&sort=view&price=20000000~25000000&size=50'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(res)
    products = []
    # Check possible structures
    if isinstance(data, dict):
        if 'data' in data:
            if isinstance(data['data'], dict) and 'products' in data['data']:
                products = data['data']['products']
            elif isinstance(data['data'], list):
                products = data['data']
        elif 'products' in data:
            products = data['products']
    elif isinstance(data, list):
        products = data
        
    print(f"Found {len(products)} products via API")
    if len(products) > 0:
        with open('d:/LogManagement/02_du-lieu-tho/laptop-thi-truong/2026-07-04_cellphones-laptop-van-phong-20-25tr.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Tên SP', 'Giá gốc (VNĐ)', 'Giá KM (VNĐ)'])
            for p in products:
                name = p.get('name', p.get('product_name', ''))
                price = p.get('price', 0)
                special_price = p.get('special_price', p.get('promotion_price', 0))
                # Only keep if special_price is between 20M and 25M
                if 20000000 <= special_price <= 25000000:
                    writer.writerow([name, price, special_price])
        print("Data saved to CSV")
except Exception as e:
    print(e)
