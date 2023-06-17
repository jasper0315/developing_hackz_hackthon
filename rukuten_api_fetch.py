import requests
import json
import time
import pandas as pd
from pprint import pprint

# 1. 楽天レシピのレシピカテゴリ一覧を取得する

res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1009993429057254143')


# 2. CategoryIdの数字を抽出
result = res.json()

large = result["result"]["large"]

test = []

for category in large:
    test.append(int(category["categoryId"]))

print(test)


# 3.　CategoryIdごとにURLを作成

base_url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
format_version = "1"
application_id = "1009993429057254143"

urls = []
for index, category_id in enumerate(test):
    if index == 100:
        print("breaked!")
        break
    url = f"{base_url}?format=json&categoryId={category_id}&formatVersion={format_version}&applicationId={application_id}"
    urls.append(url)


# 4. 楽天レシピ一覧を取得するためのcodeを作成

for code in urls:
    res = requests.get(code)
    time.sleep(0.75)
    print(res.json())
