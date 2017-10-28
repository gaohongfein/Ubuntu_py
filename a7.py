def fe(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    if n>1:
        return fe(n-1)+fe(n-2)
    
if __name__=='__main__':
    for i in range(10):
        print(fe(i))
        
