num=int(input("num value:"))
x=0
for i in range(1,num):
    x+=1
    num*=x
    print("factorial is :",num)