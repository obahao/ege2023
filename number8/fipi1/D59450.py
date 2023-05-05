#Сколько существует десятичных шестизначных чисел, делящихся на 5,
#в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?

k = []
s1 = "123456789"
s2 = "0123456789"
s6 = "05"
for a1 in s1:
    for a2 in s2:
        for a3 in s2:
            for a4 in s2:
                for a5 in s2:
                    for a6 in s6:
                        ch = a1 + a2 + a3 + a4 + a5 + a6
                        m = set(ch)
                        if len(m)==6:
                            f = 0
                            for i in range (6-1):
                                if int(ch[i]) % 2 == int(ch[i+1]) % 2:
                                    f = 1
                            if f == 0:
                                k.append(ch)
print(len(k)