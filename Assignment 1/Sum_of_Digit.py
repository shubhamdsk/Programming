# Sum of Digit

n = int(input("Enter Number:"))
sum = 0
while (n > 0):
    rem = n % 10
    sum += rem
    n = n // 10
print("Sum of Digit:", sum)

# PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py Sum_of_Digit.py
# Enter Number:12345
# Sum of Digit: 15
# (env) PS C:\Users\shubham Deshmukh\Desktop\College\Python\TYBCS\Assignment 1> py Sum_of_Digit.py
# Enter Number:456
# Sum of Digit: 15


# ************************************************************************************************************
