user=int(input("enter your number :"))
print(abs (user))

year=int(input("Enter the year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print(year ,"its a leap year")
else : print(year , "is not a leap year")

age1=int(input("Enter your age: "))
age2=int(input("Enter your age: "))
age3=int(input("Enter your age: "))
if age1>age2 and age1>age3:
    print("age1 is the oldest")
elif age2>age3 and age2>age1:
    print("age2 is the oldest")
else:
    print("age3 is the oldest")

if age1<age2 and age1<age3:
    print("age1 is the youngest")
elif age2<age3 and age2<age1:
    print("age2 is the youngest")
else:
    print("age3 is the youngest")

sum=0

for _ in range(11):
    number=float(input("Enter the number: "))
    if number<0 :
        break
    if number > 0:
        sum+=number

print("the sum is:" , sum)

age=int(input("Enter your age: "))
if age>=18:
    print("they are eligible to vote")
elif age<18:
    print("they are not eligible to vote")


num = int(input("Enter a number to find its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1

    for i in range(1, num + 1):
        result *= i
    print(f"The factorial of {num} is {result}")





