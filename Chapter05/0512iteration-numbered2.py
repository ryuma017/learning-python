strings =  ["あいうえお", "xxxyyy", "αxxβyyγ"]
print(strings)
for index, string in enumerate(strings):
    if "xxx" in string:
        strings[index] = "[検閲削除]"
print(strings)