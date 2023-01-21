input = input().split()
res = []
arr = ["a", "e", "i", "o", "u"]
for i in input:
    i = i.lower()
    s = ""
    for j in range(len(i)):
        if i[j] in arr and j%2 == 0:
            s = s + str(arr.index(i[j] + input))
        elif i[j] in arr and j%2 == 1:
            p = j%5
            if p == 0:
                p = 4
            else:
                p = p-1
            s = s + arr[p]
        else:
            s = s + i[j]
        res.append(s)
print(*res, sep=",")
    