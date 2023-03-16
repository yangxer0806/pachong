import requests


query = input("输入你喜欢的明星：")
url = f"https://www.sogou.com/web?query={query}"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=header)
print(resp.text)
resp.close()

