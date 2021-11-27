# Check Prime Number between range

start = int(input("Enter start Number:"))
end = int(input("Enter end Number:"))

for n in range(start, end + 1):
    flag = 0
    for i in range(2, n):
        if (n % i) == 0:
            flag = 1
            break
    if (flag == 0):
        print(n)

# PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py PrimeNp.py
# Enter start Number:1
# Enter end Number:15
# 1
# 2
# 3
# 5
# 7
# 11
# 13

# ************************************************************************************************************
