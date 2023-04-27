for i in range(0, 100000):
      # заменить int(input()) на i
      # заменить print(n) на if n==X: print(i)

      s = int(input())
      n = 50
      while s > 0:
          s = s // 2
          n = n - 3
          print(n)