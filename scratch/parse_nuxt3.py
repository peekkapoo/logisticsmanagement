import re
text = open('d:/LogManagement/nuxt_data.txt', encoding='utf-8').read()

matches = re.findall(r'name:"([^"]+)"', text)
print(f"Total names found: {len(matches)}")
laptops = [m for m in matches if 'Laptop' in m or 'MacBook' in m or 'Macbook' in m or 'Asus' in m or 'Lenovo' in m or 'Dell' in m or 'HP' in m]
print(f"Laptops: {len(laptops)}")

prices = re.findall(r'price:(\d+)', text)
special_prices = re.findall(r'special_price:(\d+)', text)
print(f"prices: {len(prices)}, special_prices: {len(special_prices)}")
