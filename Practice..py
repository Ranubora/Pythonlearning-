num= int(input("enter number:"))
rem= num % 2
if (rem==0):
    print("even")
else:
    print("odd") 

#Q2
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:")) 
if(a >= b and a>=c):
    print("first number is the largest ",a)
elif(b >= c):
    print("enter second number is the largest ",b)
else:
    print("third is largest")  