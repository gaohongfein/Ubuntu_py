def feb(n):
    if n==1 or n==2:
        return 1
    if n>2:
        return feb(n-1)+feb(n-2)

for month in range(1,37):
    rabit=feb(month)
    print(month,rabit)
    
