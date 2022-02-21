def tryangle(a, b, c):
    edges = [a, b, c]
    max_edge = max(a, b, c)
    edges.remove(max_edge)
    if max_edge < edges[0] + edges[1]:
        result = True
    else:
        result = False
    return result

a,b,c = (int(x) for x in input("スペース区切りで整数を3つ入力: ").split())
print(tryangle(a, b, c))