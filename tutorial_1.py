# First basics option.
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
a=x+y
print(a)


age=int(input("Enter the age you want to display"))
name=input("Enter the name")
# message="Hello Mr. "+name+" Your age is "+age   #This will throw error as it's expecting string instead of an integer

message="Hello Mr. "+name+" Your age is "+str(age)
print(message)

count = int(input("Enter the count you want to display"))
for i in range(count):
    print("Rohit")

import random

for i in range(count):
    print(random.randint(0,i))


# Comparison Operators
a=5
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

