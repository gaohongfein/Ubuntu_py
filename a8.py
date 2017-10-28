#!python3
for i in range(1,10):
    print('\n')
    for j in range(1,10):
        if j<=i:
            print("""%d*%d=%d""" % (i,j,i*j),end=" ")
#Python中print()不换行及时输出解决方案 加end
    
          
