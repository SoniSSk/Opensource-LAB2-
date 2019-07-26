list=["1","3","8","7","1","0","17","5","17"]
def duplicate(x):
    s = len(x)
    rep = []
    for i in range(s):
        k= i+1
        for j in range(k,s):
            if x[i]==x[j] and x[i] not in rep:
                rep.append(x[i])

    return rep
print(duplicate(list))
