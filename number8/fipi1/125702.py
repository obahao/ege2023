k = 0
st = "БЕЛКА"
for a1 in st:
    for a2 in st:
        for a3 in st:
            for a4 in st:
                    sl = a1+a2+a3+a4
                    if sl.count("Б") == 1:
                        k += 1
print(k)
