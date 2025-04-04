#1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print("The sum is:", sum_result)
#2
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#3
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#4
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
#5
numbers = list(range(1, 11))
for num in numbers:
    print(f"{num}^2 = {num**2}")
#6
subjects = []
scores = []
student_name = input("Enter the student's name: ")
num_subjects = int(input("Enter the number of subjects: "))
for i in range(num_subjects):
    subject = input(f"Enter name of subject {i + 1}: ")
    score = float(input(f"Enter score for {subject}: "))
    subjects.append(subject)
    scores.append(score)
average_grade = sum(scores) / num_subjects
print(f"\nStudent: {student_name}")
print(f"Average Grade: {average_grade:.2f}")

if average_grade > 70:
    print("Congratulations! You passed with a good grade! 🎉")
else:
    print("Keep going! You can improve with more effort! 💪")
#7
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)
#8
numbers = [1, 2, 3, 4, 2, 5]
element_to_remove = 2
updated_list = [x for x in numbers if x != element_to_remove]
print("Updated list:", updated_list)
#9
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))
D = int(input("Enter fourth number: "))
result = A * B * C * D
last_two_digits = result % 100
print("The last two digits of the multiplication are:", last_two_digits)
#10
X = int(input("Enter a number: "))
if X == 1:
    print(f"{X} is not a prime number.")
else:
    is_prime = True
    for i in range(2, X):
        if X % i == 0:
            is_prime = False
            break


    if is_prime:
        print(f"{X} is a prime number.")
    else:
        print(f"{X} is not a prime number.")
#11
N = int(input("Enter number of elements: "))
A = list(map(int, input("Enter the elements separated by space: ").split()))
X = int(input("Enter the number to search for: "))
if X in A:
    print("Number found at index:", A.index(X))
else:
    print("Number not found in the list.")
#12
N = int(input("Enter number of elements: "))
A = list(map(int, input("Enter the elements separated by space: ").split()))
min_value = min(A)
count_min = A.count(min_value)
if count_min % 2 == 1:
    print("Lucky array ")
else:
    print("Not lucky ")
#13
N = int(input("Enter number of elements: "))
A = list(map(int, input("Enter the elements separated by space: ").split()))
min_val = min(A)
max_val = max(A)
min_index = A.index(min_val)
max_index = A.index(max_val)
A[min_index], A[max_index] = A[max_index], A[min_index]
print("Array after swapping min and max:", A)
#14
N = int(input("Enter number of elements: "))
A = list(map(int, input("Enter the elements separated by space: ").split()))
min_value = min(A)
min_index = A.index(min_value)
print("Lowest number:", min_value)
print("Position (0-based index):", min_index)
#15
N = int(input("Enter number of elements: "))
A = list(map(int, input("Enter the elements separated by space: ").split()))
A.sort()
print("Sorted array:", A)
#16
s = input("Enter a string: ")
no_spaces = s.replace(" ", "")
print("String without spaces:", no_spaces)
#17
A = list(map(int, input("Enter the elements separated by space: ").split()))
if len(A) > 1:
    A[0], A[-1] = A[-1], A[0]
print("List after swapping first and last elements:", A)
#18
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
min_num = min(num1, num2)
hcf = 1
for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"The HCF of {num1} and {num2} is: {hcf}")





