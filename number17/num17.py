with open("17.txt", 'r') as f:
  a=[int(x) for x in f.read().splitlines()] #Открыли файл и положили число из каждой строчки в массив a
с = 0
m = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if #условие:
            s += 1
            m = max(mx, a[i] + a[j])
print(с, m)
#Массив работает как переменная с номерными ячейками, обращение к одной из таких ячеек, в нашем случае, - a[номер ячейки]