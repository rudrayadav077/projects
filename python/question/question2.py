#                   LOOPS QUESTION


#  question 1:- print natural number upto N 

# num = int (input("write a number "))
# for i in range(1,num+1):
#     print(i)

#  question 2:- print reverse of loop N  to 1 

# num = int(input("write a number to print reverse:- "))
# for i in range(num,0,-1):
#     print(i)

#  question 3:- TAKE A NUMBER AS INPUT AND PRINT ITS TABLE

# num = int(input("tell me the number would you like to print a table of it "))
# #num1 = int(input("where you want to stop the table "))

# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

#  question 4:- SUM UP TO N TERMS 

# num = int(input("tell me your number:- "))
# sum=0

# for i in range(1,num+1):
#     sum = sum+i
#     print(sum)
# print( "here is your total sum",sum)

# question 5:- factorial of a number 

# num = int(input("enter the number for factorial:- "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
#     print(fact)
# print(f"here is the  factorial of your input number:-{fact}")
    
# question 6:- print all the factor of a number 

# num = int(input("enter the numbers:- "))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i)
    
#     else:
#      print(f"this number:- {i} is not a factor of{num}({num%i==0})")

# print(f"{num}  is prime number ")

# question 7:- check the number is perfect or not 

# num = int(input("enter the number:- "))
# sum = 0
# for i in range(1,num):
#     if num%i==0:
#      sum = sum + i

# print(sum)

# question 8 :- prime number or not 

# num = int(input("enter the number to check it was a prime number or composite number "))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count= count+1
# if count == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} has {count} factor that's why its a composite number")

# # question 9 :- separate each digit of a number and print it on next line 

# # num = int(input("enter the number"))
# # digit =0
# # while(num > 0):
# #     digit= num%10
# #     print( digit)
# #     num = num//10

#question 10: check the number is pallindrome number or not 
num = int(input("enter the number "))
temp= num
rev = 0
while(num>0):
    z=num%10
    rev= rev*10+z
    num = num//10
    
if rev==temp:
    print(f"yes {rev} is a pallidromic number")
else:
    print(f"{rev} is not")
     