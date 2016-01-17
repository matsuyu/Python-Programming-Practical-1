#Summing the digits in an integer

a= int(input ("Enter the integer:"))
n=0
while a >=10:
    n=n+a%10
    a=a//10
n=a+n
print(n)
