import requests


url = "https://movie.douban.com/j/chart/top_list"
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=header, params=param)

print(resp.json())
resp.close()
