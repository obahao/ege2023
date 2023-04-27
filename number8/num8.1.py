st = "МЕТРО"
k = 0
for a1 in st:
    for a2 in st:
        for a3 in st:
            for a4 in st:
                sl = a1+a2+a3+a4
                if sl[0] in stc and sl[3] in sts:
                    k +=1
print(k)