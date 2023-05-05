with open("17-4.txt", 'r') as f:
  a=[int(x) for x in f.read().splitlines()]
sr = sum(a)/len(a)
b = []
for i in range(len(a) - 1):
    if a[i] < sr  or a[i+1] < sr:
        if (a[i] % 7 == 0 and a[i] % 3!= 0 and a[i] % 11!=0 and a[i] % 13!=0) or \
                (a[i+1] % 7 == 0 and a[i+1] % 3!= 0 and a[i+1] % 11!=0 and a[i+1] % 13!=0):
            b.append(a[i]+a[i+1])
print(len(b), min(b))