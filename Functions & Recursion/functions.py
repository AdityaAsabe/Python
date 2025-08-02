# Q1) Write a program to print the length of a list.

# cities = ['Pune','Mumbai','Hydrabad','Delhi','Bangalore','Rajasthan']
# sub = ['MATHS','CHEM','PHY','BIO','ENGLISH','MARARHI','HINDI']

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(sub)



#2) Write a program to print the elements of a list in a single line.

# sub = ["MATHS", "PHY", "CHEM", "BIO", "IT", "COMP"]

# def print_list(lst):
#     for item in lst:
#         print(item, end=" ")

# print_list(sub)



#3) Write a program to find the factorial of n.

# def cal_fact(n):
#     fact = 1
#     for i in range (1 , n+1):
#         fact*=i
#     print(fact)
# cal_fact(int(input("Enter your no:-")))



#4) Write a program to convert USD to INR.

# def converter(usd_val):
#     inr_val = usd_val * 87.20
#     print("In indian rupees :- ",inr_val)

# converter(float(input("Enter your amount in dollar:-")))



# 5) Write a program to print even or odd number.

# def print_num(num):
#     if num % 2 == 0 :
#         print(f"{num} is even")
#     else :
#         print(f"{num} is odd")

# print_num(8)



#6) Write a program to print even or odd numbers by taking as input.

# def print_num(num):
#     if num % 2 == 0 :
#         print(f"{num} is even")
#     else :
#         print(f"{num} is odd")

# num = input("Enter your numbers separated by space :-").split()

# for n in num :
#     print_num(int(n))



#7) Write a function to print your name 5 times.

# def print_name():
#     for _ in range (5):
#         print("ADITYA")

# print_name()



#8) Write a function that accepts two numbers and prints their sum.

# def add_numbers(a,b):
#     print(f"Sum = {a + b}")

# add_numbers(10,20)


 
#9) Write a function to calculate the square of a number.

# def square_num(num):
#     result = num * num
#     print(f"Square of {num} is {result}")

# square_num(int(input("Enter your number :-")))



#10) Write a function that takes a string as input and prints it in reverse order.

# def reverse_string(text):
#     reversed_text = text [::-1]
#     print(f"Reversed : {reversed_text}")

# reverse_string(input("Enter your string value :-"))



#11) Write a function to check whether a given number is prime or not.

# def prime(n):
#     for i in range(2, n-1):
#         if(n % i == 0):
#             return "NOT Prime"
#         else:
#             return "Prime"
        
# n=int(input('Enter your number: '))
# print(prime(n))



#12) Write a function that accepts a list of numbers and returns the largest number.

# def larg_num(numbers):
#     largest = numbers[0]
#     for num in numbers :
#         if num > largest :
#             largest = num
#     return largest

# numbers = list (map(int , input("Enter numbers seperated by space :- ").split()))
# print(f"{larg_num(numbers)} is a largest number")



#13) Write a function to count the number of vowels in a given string.

# def count_vow(string):
#     vowels = 'aieou'
#     string = string.lower()
#     count = 0
#     for i in string :
#         if i in vowels :
#             count+=1
#     return count

# print("Number of vowels :- ",count_vow(input("Enter your string :-")))



#14) Write a function that takes a list of numbers and returns only the even numbers.

# def print_even(num_list):
#     evens = []
#     for i in num_list :
#         if i % 2 == 0:
#             evens.append(i)
#     return evens

# num_list = list(map(int,input("Enter your numbers seperated by space :-").split()))
# print(f"Even numbers is = {print_even(num_list)}")



#15) Write a function to calculate the sum of digits of a number.

# def sum_digit(n):
#     total = 0
#     while n > 0 :
#         total += n % 10
#         n //= 10
#     return total

# n = int(input("Enter your digits :-"))
# print(f"Sum of digits is :- {sum_digit(n)}")



#16) Write a function that accepts a string and checks whether it is a palindrome.

# def palindrome_word(word):
#     word = word.lower()
#     if word == word [::-1]:
#         return "Given word is Palindrome"
#     else:
#         return "Given word is not Palindrome"
    
# word = input("Enter your word :-")
# print(palindrome_word(word))



#17) Write a function to generate and return the Fibonacci series up to n terms.

# def fibonacci(n):
#     a , b = 0 , 1
#     series = []
#     for i in range (n) :
#         series.append(a)
#         a , b = b , a + b
#     return series

# n = int(input("How many terms want :-"))
# print(f"Fibonacci numbers :- {fibonacci(n)}")



#18) Write a function to find the GCD (Greatest Common Divisor) of two numbers.

# def GCD_num(a,b):
#     while b != 0 :
#         a , b = b , a % b
#     return a

# a=int(input("Enter your value a :-"))
# b=int(input("Enter your value b :-"))
# print(GCD_num(a,b))



#19) Write a function to calculate the area of a circle when radius is given.

def area_of_circle(radius):
    pi = 3.14
    A = pi*radius*radius
    return A

radius = float(input("Enter radius of circle :-"))
print(f"Area of circle is :-{area_of_circle(radius):-.f}")