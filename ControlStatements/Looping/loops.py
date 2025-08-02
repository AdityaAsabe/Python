#1) Write a program to print the following using while loop First 10 Even numbers 

# count = 0  
# number = 2 

# print("The first 10 even numbers are:")

# while count < 10:
#     print(number)
#     number += 2
#     count += 1 


#2) Write a program to print the following using while loop First 10 Odd numbers

# count = 0
# number = 1

# print("The first 10 odd numbers are :")

# while count < 10 :
#     print(number)
#     count+=1
#     number+=2


#3) Write a program to print the following using while loop First 10 Natural numbers

# i=1
# while i<=10 :
#     print(i)
#     i+=1


#4) Write a program to print the following using while loop First 10 whole numbers

# i=0
# while i<=10 :
#     print(i)
#     i+=1


#5) Write a program to print first 10 integers and their squares using while loop.

# i=1
# while i<=10 :
#     print(i,"square is",i*i)
#     i+=1


#6) Write while loop statement to print the following series: 10, 20, 30 … … 300

# i=10
# while i<=300 :
#     print(i)
#     i+=10


#7) Write a while loop statement to print the following series 105, 98, 91 ………7

# i=105
# while i>=7 :
#     print(i)
#     i-=7


#8) Write a program to print the first 10 natural number in reverse order using while loop.

# i=10
# while i>=1 :
#     print(i)
#     i-=1


#9) Write a program to print sum of first 10 Natural numbers.

# sum = 0
# for i in range(1, 11):
#     sum += i
# print("Sum of first 10 natural numbers is:", sum)


#10) Write a program to print sum of first 10 Even numbers.

# sum = 0
# for i in range(2, 21, 2):
#     sum += i
# print(" print sum of first 10 Even numbers :",sum)


#11) Write a program to print table of a number entered from the user.

# x=int(input("Enter your number :-"))
# i=1
# while i<=10 :
#     print(i*x)
#     i+=1


#12) Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.

# x=int(input("Enter your value a="))
# y=int(input("Enter your value b="))
# if x>y :
#    x , y = y , x
# current_num = x+1
# print(f"Even numbers between {x} and {y} (exclusive) :")
# while current_num < y :
#     if current_num % 2 ==0 :
#         print(current_num)
#     current_num +=1        


#13) Write a program to check whether a number is prime or not using while loop.

# n1=int(input("Enter a  number"))
# count=0
# i=1
# while i<=n1:
#     if n1==1:
#         print("Doesn't matter")
#     if n1%i==0:
#         count+=1
#     i+=1
# if count<=2:
#     print("You Entered a Prime number")
# else:
#     print("It is not a prime number")


#14) Write a program to find the sum of the digits of a number accepted from the user.

# x=int(input("Enter your number :-"))
# y=int(input("Enter your number :-"))
# sum =0
# for i in range (x , y) :
#     sum+=i
#     print(sum)


#15) Write a program to find the product of the digits of a number accepted from the user.

# x=int(input("Enter your number a :-"))
# y=int(input("Enter your number b :-"))
# print(x*y)


#16) Write a program to reverse the number accepted from user using while loop.

# num = int(input("Enter a number: "))
# reversed_num = 0
# while num > 0:
#     remainder = num % 10
#     reversed_num = (reversed_num * 10) + remainder
#     num = num // 10
# print("Reversed number:", reversed_num)


#17) Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One

# number = input("Enter a number:- ")
# digit_names = {
#         '0': 'Zero',
#         '1': 'One',
#         '2': 'Two',
#         '3': 'Three',
#         '4': 'Four',
#         '5': 'Five',
#         '6': 'Six',
#         '7': 'Seven',
#         '8': 'Eight',
#         '9': 'Nine'
#     }

# for digit in number:
#     print(digit_names[digit], end=" ")
# print()



#18) Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.

# n=int(input("Enter the number of trems :-"))

# a=0
# b=1
# count=0

# if n < 0 :
#     print("Enter a positive integer :-")
# else :
#     print("Fibonacci series :-")
#     while count < n :
#         print(a,end="")
#         a , b = b , a+b
#         count+=1



#19) Write a program to print the factorial of a number accepted from user.

# while True:
#     n = int(input("Enter your number :- "))
#     if n < 0:
#         print("Invalid input. Please enter an integer.")
#     else:
#         break

# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(f"The factorial of {n} is {factorial}.")



#20) Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.

# total = 0

# while True:
#     num = int(input("Enter a number: "))
#     total += num

#     choice = input("Do you want to enter another number? (yes/no): ").lower()
#     if choice != "yes":
#         break

# print(f"The sum of all numbers entered is {total}.")



#21) Write a program to convert Decimal to Binary.

# decimal = int(input("Enter a decimal number: "))

# binary = ""

# if decimal == 0:
#     binary = "0"
# else:
#     while decimal > 0:
#         remainder = decimal % 2
#         binary = str(remainder) + binary
#         decimal = decimal // 2

# print("Binary representation:", binary)




#22) Write a program to convert Binary to Decimal.

# binary = input("Enter a binary number: ")
# decimal = 0

# binary = binary[::-1]

# for i in range(len(binary)):
#     if binary[i] == '1':
#         decimal += 2 ** i

# print(f"The decimal equivalent is {decimal}")




#23) Write a program to accept 10 numbers from the user and display it’s average

# numbers = []

# for i in range (10):
#     num=float(input(f"Enter your numbers {i + 1} :-"))
#     numbers.append(num)

# average= sum(numbers) / len(numbers)
# print(f"The average of entired numbers :-{average}")



#24) Write a program to accept 10 numbers from the user and display the largest & smallest number.

# numbers=[]

# for i in range (10):
#     num=float(input(f"Enter your numbers {i + 1}:-"))
#     numbers.append(num)

# largest= max(numbers)
# smallest= min(numbers)

# print(f"The largest number is :- {largest}")
# print(f"The smallest number is :- {smallest}")



#25) Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.(exclusive both numbers)

# x=100
# y=500

# for num in range (x , y) :
#     if num %13==0 and num%3!=0 :
#         print(num)