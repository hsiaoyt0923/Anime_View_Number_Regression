import requests
import re


# 從提供free proxy的網站上取得ip、port
response = requests.get("https://example.com/")
# 「\d+」代表數字一個位數以上
proxy_ips = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)

valid_ips = []

# 嘗試透過proxy連線任一網站
for ip in proxy_ips:
    try:
        result = requests.get('https://api.seeip.org/jsonip',
                              proxies={'http': ip, 'https': ip}, timeout=5)
        print(result.json())
        valid_ips.append(ip)
    except:
        print(f"{ip} invalid")


# 將有效ip存檔
with open('proxy_list.txt', 'w') as file:
    for ip in valid_ips:
        file.write(ip + '\n')
    file.close()
