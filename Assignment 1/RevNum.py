# Print Reverse Number

n = int(input("Enter Number:"))
rev=0

while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10

print("Reverse of number is:{}".format(rev))

# PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py RevNum.py
# Enter Number:12345
# Reverse of number is:54321

# ************************************************************************************************************
