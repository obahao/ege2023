st = "КЛРТ"
n = 0
for a1 in st:
    for a2 in st:
        for a3 in st:
            for a4 in st:
                sl = a1+a2+a3+a4
                n+=1
                if n == 67:
                    print(sl)