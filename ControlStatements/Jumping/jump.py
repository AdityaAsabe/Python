#1) Write a program to print numbers from 1 to 100. Stop the loop if a number divisible by 17 is found.
 
# for num in range (1,100):
#     if num % 17==0 :
#       print(f"Stopping at {num} because it is divisible by 17.")
#       break
#     print(num)



#2) Read numbers from the user until a negative number is entered. Use break to stop and display the total of all positive numbers

# total = 0

# while True :
#     num=float(input("Enter a numbers (negative number to stop) :- "))
#     if num < 0 :
#         break 

#     total +=num
# print(f"Total of all positive numbers is :- {total}")



#3) Search for the first number between 100 and 200 that is divisible by both 9 and 6. Use break to stop after finding it.

# x=100
# y=200

# for num in range (x , y) :
#     if num % 9 == 0 and num % 6 == 0 :
#         print("The first number between 100 and 200 divisible by both 9 and 6 is:", num))
#         break



#4) Loop through characters in a string. Stop the loop when you find the first vowel.

# text=input("Enter your string :-")

# for i in text :
#     if i.lower() in 'aeiou':
#         print(f"First vowel found :- {i}")
#         break
#     else:
#         print("Vowels not found")



#5) Write a program to simulate a basic password check. Ask for a password in a loop and use break when the correct one is entered.

# passw = "adityaasabe07"

# while True :
#     pass2 = input("Enter your password :-")
#     if passw == pass2 :
#         print ("Entered password is right")
#         break
#     else :
#         print("Entered password is wrong , re-enter right password.")



#6) Print even numbers between 1 and 50. Stop the loop if the number is greater than 40.

# for i in range (2,51,2):
#     if i > 40:
#         break
#     print(i)



#7)  Write a program to check prime numbers from 10 to 50. Stop the loop if a number is not prime.

# for num in range(10, 51):
#     is_prime = True

#     if num < 2:
#         is_prime = False
#     else:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break

#     if is_prime:
#         print(num)
#     else:
#         print(f"{num} is not prime. Stopping the loop.")
#         break



#8) Print all numbers from 1 to 50 except those divisible by 5 using continue.

# for i in range (1, 51):
#     if (i%5==0):
#         continue
#     print(i)



#9) Display all characters in a string except the vowels using continue.

# string='sdfghaournjidsn'

# for i in string :
#     if i.lower() in 'aieou':
#         continue
#     print(i)



#10) Write a program that prints numbers from 1 to 20, skipping every third number using continue.

# for i in range (1,21):
#     if i%3==0 :
#         continue
#     print(i)



#11) Print all lowercase letters in a string, skipping uppercase letters with continue.

# string='aSdBkbhuSNddsbhsIH'

# for i in string:
#     if i==i.upper():
#         continue
#     print(i)



#12)  From numbers 1 to 100, print only those not divisible by 2 or 3 using continue.

# for i in range(1, 101):
#     if (i%2==0  or i%3==0):
#         continue
#     print(i)



#13) Accept 10 numbers from the user. Skip negative numbers and only add the positive ones.

# total = 0

# print("Enter 10 numbers:")

# for i in range(10):
#     num = int(input(f"Enter number {i+1}: "))
#     if num < 0:
#         continue
#     total += num

# print("Sum of positive numbers is:", total)



#14) Loop through a list of fruits and skip the fruit named "banana" using continue.

# fruits=['mango','apple','banana','cheery','pineapple']

# for fruit in fruits :
#     if fruit=='banana':
#         continue
#     print(fruit)



#15) Write a program that loops from 1 to 10 and uses pass for even numbers.

# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i)



#16) Create a function that is defined but not yet implemented using the pass statement.

# def my_funcions():
#     pass



#17) Write a class with a method stub using pass. Instantiate the class and call the method without errors.

# class Myclass :
#     def my_method(self):
#         pass
# obj=Myclass()
# obj.my_method



#18)  Loop through numbers from 1 to 30:(* If divisible by 3, skip using continue.* If number is 25, stop using break.* Otherwise, print the number.)

# for i in range (1, 31):
#     if i%3==0:
#         continue
#     if i==25:
#         break
#     print(i)



#19) Accept inputs from the user in a loop:(* If input is a blank string, use pass.* If it's "exit", break the loop.* Otherwise, print the input in uppercase.)

# while True:
#     user_input=input("Enter something (type 'exit' for quit): ")

#     if user_input=="":
#         pass
#     elif user_input.lower()=='exit':
#         break
#     else:
#         print(user_input.upper())



#20) Read 10 numbers:(* If number is zero, skip using continue.* If number is negative, stop using break.* Use pass for numbers greater than 100.* Print and sum the rest.)

# total = 0

# for i in range(10):
#     num=int(input(f"Enter number {i+1}:"))

#     if num == 0:
#         continue
#     elif num < 0:
#         break
#     elif num > 100:
#         pass
#     else:
#         print("Accepted:",num)
#         total += num

# print("Sum of accepted numbers:", total)