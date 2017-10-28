def getReward(I):
    if I<=10:
        reward=0.1*I
    elif 10<I<=20:
        reward=(I-10)*0.075+getReward(10)
    elif 20<I<=40:
        reward=(I-20)*0.05+getReward(20)
    return reward

if __name__=='__main__':
    while(1):
        i=int(input("How much I\n"))
        j=getReward(i)
        print(j)
