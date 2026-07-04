import re
text = open('d:/LogManagement/nuxt_data.txt', encoding='utf-8').read()

names = list(re.finditer(r'name:"(Laptop.*?)"', text))
for m in names[:5]:
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 150)
    print("---")
    print(text[start:end])
