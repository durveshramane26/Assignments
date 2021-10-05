
no = int(input("Enter the ending number of the range"))
 
for n in range(1, no+1):
    sum=0

    for i in range(1, n):
        if n%i==0:
            sum += i

    if n==sum:
        print(n)
