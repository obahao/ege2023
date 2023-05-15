print ("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not((not x or w) and (y or z)) or ((z == x) or (w and not y))):
                    print (x, y, z, w)