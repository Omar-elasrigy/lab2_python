def multiply(num):
    list2=[]
    for n in range(1,num+1):
        list=[]
        n2=1
        while n2<=n:
            if n==1:
                list.append(1)
                break;
            elif n2 <=n:
                list.append(n*n2)
            n2+=1
           
        list2.append(list)
    print(list2)
number=int(input("please enter a number: "))
multiply(number)
