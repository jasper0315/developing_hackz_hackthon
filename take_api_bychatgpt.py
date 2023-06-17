import requests

# APIキーを設定します
api_key = "YOUR_API_KEY"

# APIのURLを構築します
base_url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426"
url = f"{base_url}?format=json&applicationId={api_key}"

# APIリクエストを送信し、レスポンスを取得します
response = requests.get(url)

# レスポンスのステータスコードを確認します
if response.status_code == 200:
    # レスポンスのJSONデータを取得します
    recipe_data = response.json()

    # レシピ一覧の処理
    recipes = recipe_data['result']
    for recipe in recipes:
        print(recipe['recipeTitle'])
else:
    print("APIリクエストが失敗しました。")