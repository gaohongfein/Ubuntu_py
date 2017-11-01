#import string
l=[]
l=input('请输入')
a=0
b=0
d=0
for c in l:
    if c.isalpha():
        a+=1
    if c.isspace():
        b+=1
    if c.isdigit():
        d+=1



print(a,b,d)
        
