def Occ(number):
    for i in range(0,10):
        count=0;
        temp=number;
        while temp>0:
            digit=temp%10
            if digit==i:
                count=count+1
            temp=temp//10;
        if count>0:
            print(i,"\t",count)

number=int(input("Enter any Number"))
print("Digit\tCount")
Occ(number)

