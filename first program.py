print("hello world")
name ="Raanu bora"
age =24
print("my name is:", name)
print(" my age is:", age)
print(type(name))
print(type(age))
age =24
old= False
a=False
print(type(old))
print(type(a))
a=2
b=5
sum= a+b
print(sum)
#arithmatic operator
a=5
b=2
sum =(a+b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#relational operators
a=50
b=20
print(a==b)#False
print(a!=b)#True

print(a>=b)#True
print(a>b)#True
print(a<=b)#False
print(a<b)#False
#assigment operators
num =10
num =num + 10
print("num:", num)
# logical operators
a=50
b=30
print( not False )
print(not (a>b))
name = input ("enter your name")
print( "welcome", name)
name =input("enter name:")
age =input("enter age:")
first =int (input("enter first:"))
second = int (input ("enter second:"))
print("sum =", first + second)
side = float(input("enter square side:"))
print("area=", side * side)
a = float(input("enter first:"))
b= float(input("enter second:"))
print("avg=", (a+b)/2)
str1 ="this is a string.\nwe are creating it in python" 
print(str1)
str1 = " this is  string.\t we are creating it in python"
print (str1)
str1 ="hello"
str2="world"
finalstr =str1+str2
print(finalstr)
len1=len(str1)
len2=len(str2)
print(len2)
str="hello world"
print(str[4])
str="hello world"
print (str[1:5])
print(str[0:6])

str ="I am studying python from apnacollege."
print(str.endswith("ege"))
print(str.capitalize())
print(str.replace("o","a"))
print(str.find("python"))
print(str.count("from"))
name= input( "enter your name :" )
print("length of your name is ",len(name))
str= "hii $I am the $ symbol $99.99"
print(str.count("$"))
age= 21
if(age>=18):
    print("can vote")
    print("can drive")
age= 21
if(age>=18):
    print("can vote")
    print("can drive")
    light="green"
if(light=="red"):
    print("stop")
if (light=="green"):
   print("go")
   print ("end of the code")    
num=5
if (num>2):
    print("greater than 2")
elif(num>3):
    print ("greater than 3")
light="pink"
if(light=="red"):
    print("stop")
elif (light=="green"):
   print("go")
else:
    print("light is broken")
print ("end of the code") 
age=24
if(age>=18):
   print("can vote")
else:
   print("cannot vote")

marks=74

if(marks>=90):
    print="A"
elif(marks>=80 and marks< 90):
    print="B"
elif(marks>=70 and marks< 80):
    print="C"
else :
    grade="D"
print("grade of the student->",grade)
            
marks = int(input("enter student marks :"))

if(marks>=90):
    grade="A"
elif(marks >=80 and marks < 90):
    grade="B"
elif(marks >=70 and marks < 80):
    grade="C"
else :
    grade="D"

    print("grade of the student->",grade)
age=34
if(age >= 18):
    print("can drive")
else:
    print("cannot drive")
#nesting
age = 34
if( age >=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print('cannot drive')
 
#nesting
age = 93
if( age >=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print('cannot drive')

num=14
rem=num % 2
if (rem==0):
    print("even")
else:
    print("odd") 

num= int(input("enter number:"))
rem=num % 2
if (rem==0):
    print("even")
else:
    print("odd")       
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))   
if(a >= b and a>=c):
    print("first number is the largest ",a)
elif(b >= c):
    print("enter second number is the largest ",b)
else:
    print("third is largest")        
x =int(input("enter number:"))
if (x %7 ==0):
    print("multiple of 7")
else:
    print("not multiple of 7")                          
x=int(input("enter number:"))
if (x %5 ==  0):
    print("multiple of 5")
else:
    print("not multiple of 5")  
marks = [94.4,87.5,97.2,66.4,45.1]
print(marks)
print(type(marks))   
marks = [94.4,87.5,97.2,66.4,45.1]
print(marks)
print(type(marks))
print (marks[0])
print(marks[1])
marks = [94.4,87.5,97.2,66.4,45.1]
print(marks)
print(len(marks))
student=["karan",19 ,"delhi"]
print(student)   
student=["karan",19 ,"delhi"]
print(student[0])
student[0]= "Arjun"
print(student)
marks=[85,94,76,63,48]
print(marks[1:4])
marks=[85,94,76,63,48]
print(marks[1:])
marks=[85,94,76,63,48]
print(marks[-3:-1])
list = [2,1,3]
list.append(4)
print (list)
list = [2,1,3]
list.append(4)
print(list.sort())
list = [2,1,3]
list.reverse()
print(list)
list = [2,1,3]
list.insert(1,5)
print(list)
list = [2,1,3,1]
list.pop(2)
print(list)
tup=(2,1,3,1)
print(type(tup))
tup=( 1)
print(tup)
print(type(tup))
tup=( )
print(tup)
print(type(tup))
tup= (1,2,3,4)
print(tup[1:3])
tup= (1,2,3,4)
print(tup.index(2))
tup=(1,2,3,4,2,4,2)
print(tup.count(2))
movies=[]
input("enter 1st movie:")
input("enter 2nd movie:")
input("enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
list1 = [1,2,1]
list2 =[1,2,3]
copy_list1 =list1.copy()
copy_list1.reverse()
if (copy_list1 ==list1):
    print("palindrome")
else:
    print("not palindrome")
Grade =("C","D","A","A","B", "B","A")
print(grade.count("A"))
grade =["C","D","A","A","B", "B","A"]
grade.sort()
print(grade)
info = {
    "key":"value",
    "name" : "Ranu",
    "learning" : "coding"
}
print(info)
info = {
    "key":"value",
    "name" : "Ranu",
    "learning" : "coding",
    "age" : 35,
    "is-adult" : True,
    "marks" : 94.4
}
print(info)
info = {
    "name" : "Ranu",
    "subject" : ["python", "c"," java"],
     "topics" : ("dict", "set"),
     "age" : 35,
    "is-adult" : True,
    "marks" : 94.4
}
print(info)
info = {
    "name" : "Ranu",
    "subject" : ["python", "c"," java"],
     "topics" : ("dict", "set"),
     "age" : 35,
    "is-adult" : True,
    "marks" : 94.4
}
print(type(info))
null_dict ={}
print(null_dict)
null_dict ={}
null_dict["name"]= "hello world"
print(null_dict)
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
#nested dictionary
print(student)
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
#nested dictionary
print(student["subject"]) 
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
#nested dictionary
print(student["subject"]["chemistry"])
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(student.keys())
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(len(student))
print(student.keys())
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(len(list(student.keys())))
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(student.values()) 
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(list(student.values()))
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(student.items())
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(list(student.items()))

student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(pairs[0])
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
print(student["name"])
print(student.get ("name"))
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}
student.update({"city" : "delhi"})
print(student)
student={
    "name" : "Nidhi jain",
    "subject": {
        "physics":  97,
        "chemistry" : 98,
              "maths" : 95     
    }
}

new_dict = {"name": "neha kumar","age":16}
student.update(new_dict)
print(student)
collection ={1,2,3,4}
print(collection)
print(type(collection))
collection ={1,2,3,4,2,2,"hello world", "hello","hello"}
print(collection)
print(type(collection))
collection ={1,2,3,4,2,2,"hello world", "hello","hello"}
print(collection)
print(len(collection))
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apna college")
collection.add((1,2,3))
print(collection)
print(len(collection))
collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apna college")
collection.add((1,2,3))
collection.clear()
collection ={"apna college","hello","world","coding","python"}
print(collection.pop())
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1)
print(set2)
et1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))
print(set1)
print(set2)
set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))
print(set1)
print(set2)
dictionary ={
    "cat" :"a small animal",
    "table" : ("a piece of furniture","lists of facts and figure")
    }
print(dictionary)

subjects={
"python","java","c++","python","javascript","java","python","java","c++","c"
}
print(subjects)
marks ={}
x= int(input(" enter physics:" ))
marks.update({"physics":x})
x=int(input("enter chemistry:"))
marks.update({"chemistry":x})
x=int(input("enter maths:"))
marks.update({"maths":x})
print()
#Q1
i=1
while i<= 100:
    print(i)
    i+= 1

count = 1
while count <= 5:
    print("hello")
    count +=1

    print(count)

i = 1
while i<=5:
    print (i)
    i +=1
    
print("loop ended")

i = 5
while i>=1:
    print (i)
    i -=1
    
print("loop ended")


#Question1
i =1
while i <=100 :
    print(i)
    i+= 1

 #Question2
i =100
while i >=1 :
    print(i)
    i-= 1

 #Question3
i =1
while i <=10:
    print(3*i)
    i+= 1

    #Question4
num =[11,4,9,16,25,36,49,64,81,100]
idx = 0
while idx <len(num):
    print(num[idx]) #num(0),num(1), num(2).....
    idx += 1

i =1
while i <=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")       
   
i =1
while i <=5:
    if(i==3):
     i+=1
    continue
    print(i)
    i+=1

nums = [1,2,3,4,5]

for val in nums:
    print (val )

veggies = ["ladyfinger", "tamato" ,"patato","cucumber" ]

for val in veggies:
    print(val)

tup = [1,2,3,4,5,6,7,8,9,]

for num in tup:
    print(num)

str ="hello world"

for char in str :
    print(char)

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

seq = range(5)

for i in seq:
    print(i)

for i in range (10): #range(stop)
    print(i)

for i in range (2,10): # range(start,stop)
    print(i)

    #Q1
for i in range(1,101):
    print(i)

for i in range (2,10,2): #range(start,stop,step)    
    print(i)

for i in range(2 , 100,2): 
    print(i)

for i in range(1 , 100,2): 
    print(i)

#Q2
for i in range(100,0,-1):
    print(i)


#Q3
n= int(input("enter number :"))

for i in range (1,11):
    print(n*i)

for i in range (5):
    pass
print ("some useful work")

n= 5

for i in range(1,n+1):
   sum +=i
   
   n= 5

sum = 0
for i in range(1,n+1):
    sum +=i

    print("total sum = ", sum )

#Q1
cities =["delhi","mumbai","noida","chennai","gurgaon","pune"]
heros = ["saktiman","thor","captain america","iron man"]

def print_len(ist):
    print(len(list))

    print_len(cities)
    print_len(heros)
    

      

         

 
    
    
















              














               







































































































