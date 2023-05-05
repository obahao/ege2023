st = "АМРТ"
k = 0
for a1 in st:
    for a2 in st:
        for a3 in st:
            for a4 in st:
                for a5 in st:
                    sl = a1+a2+a3+a4+a5
                    while a1 == 'М':
                        k += 1
                        print(k)