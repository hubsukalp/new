print("hello world")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if(a>b):
  print("largest number is ",a)
elif(a<b):
  print("largest number is ",b)
else:
  print("Both numbers are equal")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)