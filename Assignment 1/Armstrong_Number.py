
#Armstrong Number

n = int(input("Enter Number:"))
num=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if num==sum:
    print(num,"is an armstrong")
else:
    print(num,"is not an armstrong")


# PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py Armstrong_Number.py
# Enter Number:153
# 153 is an armstrong
# (env) PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py Armstrong_Number.py
# Enter Number:121
# 121 is not an armstrong

# ************************************************************************************************************

