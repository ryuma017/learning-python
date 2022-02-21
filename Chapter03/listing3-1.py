# 値段の一覧を与えられた表示幅で出力する

width = int(input("表示幅を入力してください:"))   # ①表示幅を指定

price_width = 10
item_width = width - price_width

# ②formatで書式指定子になる文字列を作成し、変数header_fmtとfmtに格納
header_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
fmt        = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)

print("=" * width)

# ③変数header_fmtの文字列を書式指定子として使用
print(header_fmt.format("Item", "Price"))

print("-" * width)

# ③変数fmtの文字列を書式指定子として使用
print(fmt.format("Apples", 0.4))
print(fmt.format("Pears", 0.5))
print(fmt.format("Cantaloupes", 1.92))
print(fmt.format("Dried Apricots (16 oz.)", 8))
print(fmt.format("Prunes (4 lbs.)", 12))

print("=" * width)