import requests

# 楽天レシピ検索API (BooksGenre/Search/)のURL
url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1009993429057254143"

# URLのパラメータ
param = {
    # 前手順で取得したアプリIDを設定する
    "applicationId" : "1009993429057254143",
    "keyword" : "肉",
    "format" : "json"
}

# APIを実行して結果を取得する
result = requests.get(url, param)