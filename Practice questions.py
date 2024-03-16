#lec = 1
#Q1.write a program to input 2 numbers and print their sum .
first =int (input("enter first:"))
second = int (input ("enter second:"))
print("sum =", first + second)

#Q2 write a program to input side of square and print its area.
side = float(input("enter square side:"))
print("area=", side * side)

#Q3 write a program to input 2 floating point numbers and print their avg.
a = float(input("enter first:"))
b= float(input("enter second:"))
print("avg=", (a+b)/2)

#Q4 write a program to input 2 int numbers ,print True if a is greater then or equals to b.If not print False
a= int(input("enter first :"))
b= int(input("enter second :"))

print(a>=b)

# #lec =2
# #Q1

# num= int(input("enter number:"))
# rem= num % 2
# if (rem==0):
#     print("even")
# else:
#     print("odd") 

#Q2
a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:")) 
# if(a >= b and a>=c):
print("first number is the largest ",a)
elif(b >= c):
print("enter second number is the largest ",b)
else:
print("third is largest")  

# #Q3
    
# x =int(input("enter number:"))
# if (x % 7 ==0):
#    print("multiple of 7")
# else:
#     print("not multiple of 7")  

#lec =3
#Q1
# movies=[]
# mov1 = input("enter 1st movie:")
# mov2 = input("enter 2nd movie:")
# mov3 = input("enter 3rd movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#Q2
list1 = [1,2,1]
list2 =[1,2,3]
copy_list1 =list1.copy()
copy_list1.reverse()
if (copy_list1 ==list1):
    print("palindrome")
else:
    print("not palindrome")
    
#Q3
grade =["C","D","A","A","B", "B","A"]
grade.sort()
print (grade)

#lec=4

#Q1

dictionary ={
    "cat" :"a small animal",
    "table" : ("a piece of furniture","lists of facts and figure")
    }
print(dictionary)

#Q2

subjects={
"python","java","c++","python","javascript","java","python","java","c++","c"
}
print(subjects)
print(len(subjects))

#Q3

marks ={}
x= int(input(" enter physics:" ))
marks.update({"physics":x})
x=int(input("enter chemistry:"))
marks.update({"chemistry":x})
x=int(input("enter maths:"))
marks.update({"enter maths":x})

print(marks)

#Q4


#lec =7

#Q1

#Q2
with open("practice.txt","r")as f:
    data=f.read()
    new_data = data.replace("java","python")
    print(new_data)
with open("practice.txt","w")as f:
     f.write(new_data)




#lec=8
#Q1

class student:
    def __init__(self ,name , marks):
        self.name =name
        self.marks= marks

    def get_avg(self):
      sum=0
      for val in self.marks:
        sum+=val
      print("hii",self.name,"your avg score is :" ,sum/3)            

s1= student("karan kumar", [99,97,98])
s1.get_avg()