num=99
l=[]
m=[]
sum=0
for i in range(2,201):
    for j in range(2,(int)(i/2)+1):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)        
            
for i in range(2,200):
    for k in l:
         if num%k==0:
            m.append(k)
            num=num/k
            break
print(m)
    
            
    
    
