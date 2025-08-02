#1) write a program to check given is greater than 10.

# x=int(input("Enter your number :-"))
# if x>10 :
#     print(x,"Is greater than 10")


#2) Check if a number is positive, negative, or zero.


# x=int(input("Enter your value"))
# if x==0:
#     print("zero")
# elif x>0 :
#     print("positive")
# else :
#     print("negative")


#3) Check if a number is even or odd.


# x=int(input("Enter your number :-"))
# if x%2==0 :
#     print("Number is even")
# else :
#     print("Number is odd")


#4) Check if a person is eligible to vote (age ≥ 18).


# x=int(input("Enter your age :-"))
# if x>=18 :
#     print("a person is eligible to vote")
# else :
#     print("a person is not eligible to vote")


#5) Check if a year is a leap year.


# year=int(input("Enter your year :-"))
# if (year % 4==0 and year % 100 != 0) or (year % 400 == 0) :
#     print (year," is leap year")
# else :
#     print(year,"is not leap year ")


#6) Find the greatest of two numbers.


# x=int(input("Enter your number a :-"))
# y=int(input("Enter your number b :-"))
# if x>y :
#     print(x," is greatest number")
# else :
#     print(y," is greatest number")


#7) Find the largest among three numbers.


# x=60
# y=30
# z=20
# if (x>y and x>z) :
#     print(x,"is largest")
# elif (y>x and y>z) :
#     print(y,"is largest")
# else :
#     print(z,"is largest")


#8) Check whether a character is a vowel or consonant.////////

# value=str(input("Enter youe character :- "))
# a=("a","o","e","u")
# if value in a :
#     print("It is vowels")
# else:
#     print("It is consonant")


#9) Check if a number is divisible by both 3 and 5.

# x=int(input("Enter your number :-"))
# if (x%3==0 and x%5==0):
#     print("True")
# else :
#     print("False")


#10) Check if a given number is within the range 1 to 100.

# x=int(input("Enter your number :-"))
# if (x>=1 and x<=100) :
#     print("True")
# else :
#     print("False")


#11) calculater 

# a=int(input("Enter your value a:-"))
# b=int(input("Enter value b :-"))
# o=input("operetor for given values :-")

# if o=="+":
#     print(a+b)
# elif o=="-" :
#     print(a-b)
# elif o=="*" :
#     print(a*b)
# elif o=="/" :
#     print(a/b)
# elif o=="**" :
#     print(a**b)
# else :
# print("None")


#12) Write a program that takes a person's weight and height as input and prints their BMI categor

# h=float(input("Enter your height :-"))
# w=float(input("Enter your weight :-"))
# bmi=w/h**2
# if bmi<18.5 :
#     print("Underweight")
# elif (18.5<=bmi and bmi>=24.9) :
#     print("Normal weight")
# else :
#     print("O")


#13) Write a program that takes a student's score as input and prints their grade based on the following criteria:

# x=int(input("Enter your mark :-"))
# if 90<=x<=100 :
#     print("Grade A")
# elif 80<=x<=89 :
#     print("Grade B")
# elif 70<=x<=79 :
#     print("Grade C")
# elif 60<=x<=69 :
#     print("Grade D")
# else :
#     print("Fail")

#14) write a program for applicable for liceance

# age=int(input("Enter your age :-"))
# if age>18 :
#     print("Your are applicable for liceance")
# else :
#     print("Your are not applicable for liceance")


#15)  write a program for Take three numbers as input and print the largest among them.

#x=int(input("Enter your number :-"))
#y=int(input("Enter your number :-"))
#z=int(input("Enter your number :-"))
#if (x>y and x>z) :
#     print(x,"is largest")
#elif (y>x and y>z) :
 #    print(y,"is largest")
#else :
#     print(z,"is largest")


#16) Write a program for Create a condition that checks if a triangle is equilateral, isosceles, or scalene given side lengths.

# a=float(input("Enter triangle side a :-"))
# b=float(input("Enter triangle side b :-"))
# c=float(input("Enter triangle side c :-"))

# if a==b==c :
#         print("Triangle is equilateral ")
# elif (a==b) or (b==c) or (a==c) :
#         print("Triangle is isosceles ")
# else:
#         print("Triangle is scalene")



#17)  Create a login system that checks for both username and password correctness.

# usr=str("adityaasabe07")
# pp=str("ad22as44")

# x=str(input("Enter your username :-"))
# y=str(input("Enter your password :-"))

# if usr==x or pp==y  :
#     print("Correct")
# else:
#     print("Incorrect")



#18) Write a program that determines whether a character is uppercase, lowercase, a digit, or a special character.

# char = input("Enter a character: ")

# if 'A' <= char <= 'Z':
#     print("Uppercase letter")
# elif 'a' <= char <= 'z':
#     print("Lowercase letter")
# elif '0' <= char <= '9':
#     print("Digit")
# else:
#     print ("Special character")



#19) A store offers a 10% discount if the total bill is over \$100. Write a condition that calculates the final amount.

# x=float(input("Enter your bill amount :-"))

# if x>100:
#     a=(x/100)*90
#     print("Your amount applicable for 10% offer so final amount is :- ",a)
# else :
#     print("Your amount is less than offer criteria , so final amount is :-",x)



#20) Write a condition to determine if a given time is AM or PM based on a 24-hour input.

# hour=int(input("Enter your time :-"))

# if hour < 12 :
#     print("Time is AM")
# elif hour < 12 and hour < 24 :
#     print("TZime is PM")
# else :
#     print("Time is PM")