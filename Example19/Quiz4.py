'''
        *
       ***
      *****
     *******
    *********

'''
for i in range(0,11,2):
    for j in range(10,i,-2):
        print(" ",end='')
    for i in range(1, i):
        print("*", end='')
    print("")
