# 単純なデータベース。get()を使うバージョン
#
people = {
    "渋谷": {
        "内線": "2341",
        "メール": "taro-shibuya"
    },
    "恵比寿": {
        "内線": "9102",
        "メール": "hanako-ebisu"
    },
    "上野": {
        "内線": "3158",
        "メール": "jiro-ueno"
    }
}

# 「ユーザーに表示するメッセージ」と「記憶するデータのキー」との対応を記憶
lables = {
    "内線": "内線番号",
    "メール": "メールアドレス"
}

name = input("名前を入力してください:")

# 内線番号とメールアドレスのどちらを調べるのか尋ねる
request = input("内線電話は t を、メールアドレスは m を入れてください:")

if request == "t": key = "内線"
if request == "m": key = "メール"

# getを使ってデフォルト値を出力する
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, "未登録")

print(f"{name}さんの{lables}は {result} です。")