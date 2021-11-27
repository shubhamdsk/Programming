# Prime Number

num = int(input("Enter start Number:"))
flag = 0
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = 1
            break
if flag:
    print(num, "is not a number prime")

else:
    print(num, "is a prime number")

# PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py PrimeOrNot.py
# Enter start Number:6
# 6 is not a number prime
# (env) PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py PrimeOrNot.py
# Enter start Number:7
# 7 is a prime number
# (env) PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py PrimeOrNot.py
# Enter start Number:10 
# 10 is not a number prime

# ************************************************************************************************************
