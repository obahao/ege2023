print ("w x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not x and y) or (x == z) or not w):
                    print (w,x,y,z)