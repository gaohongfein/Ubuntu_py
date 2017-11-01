l=[]
sum=0
for i in range(101,201):
    
    for j in range(2,(int)(i/2)+1):
        if i%j==0:
            break
    else:
        l.append(i)
        sum=sum+1

print(l)
print(sum)
            
