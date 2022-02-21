while True:
    try:
        total_price = int(input("合計金額を入力: "))
        num = int(input("人数を入力: "))
        if total_price < 0 or num < 0:
            print("正の数を入力してください")
            continue
        else:
            result = total_price / num
            print(f"一人あたりの料金は{result}円です")
            break

    except ValueError:
        print("数値を入力してください")
    
    except ZeroDivisionError:
        print("誰も参加しなかったのですか？")

    except:
        print("予期せぬエラー")
        break