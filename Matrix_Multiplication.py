def Matrix():
    a=[]
    for i in range(3):
        b=[]
        for j in range(3):
            c=int(input("Enter the 1st matrix"))
            b.append(c)
        a.append(b)

    for i in range(3):
        for j in range(3):
            print(a[i][j],end="\t")
        print("\n")

    x=[]
    for i in range(3):
        y=[]
        for j in range(3):
            z=int(input("Enter the 2nd matrix"))
            y.append(z)
        x.append(y)

    for i in range(3):
        for j in range(3):
            print(x[i][j],end="\t")
        print("\n")
    
    p=[]
    for i in range(3):
        q=[]
        for j in range(3):
            r=a[i][j]*x[i][j]
            q.append(r)
        p.append(q)
    print("\n")
    print("Multiplication of two matrix is :")
    
    for i in range(3):
        for j in range(3):
            print(p[i][j],end="\t")
        print("\n")

Matrix()
