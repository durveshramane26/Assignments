def Palindrome(str1):
    str2=""
    for i in str1:
        str2=i+str2
    if str2==str1:
        print(str1 ,"is palindrome")
    else:
        print(str1 ,"is not  palindrome")
str1=input("Enter the string")
Palindrome(str1)
