#1 accept two numbers and print greatest between them 

num1 = int (input ( "Enter the First number:- "))
print("\n")
num2 = int (input ("Enter the second number:- "))
if num1>num2:
    print("number 1 is the greatest number",num1)
elif num1<num2:
    print("number 2 is the greatest number:-", num2)
else:
    print(f"both num1:-{num1} and num2:-{num2} are equal")

# QUESTION 2 
# ACCPET THE GENDER FROM THE USER US CHAR AND PRINT THE GREETING MESSAGE LIKE 
# GOOD MORNING SIR IF HE WAS MALE.

gender = input("Please tell me your gender:- ")
if gender =="male" or "MALE" or "Male":
    print("good morning sir")
elif gender == "female" or "Female" or "FEMALE":
    print("good morning mam")
else :
    print("good morning") 


# QUESTION 3 
# ACCPET THE NUMBER AND CHECK WEATHER THE NUMBER IS EVEN OR ODD 

num = int (input("Enter the number:- "))
if num%2==1:
    print(f"{num} is odd")
else:
    print(f"the {num} is even")


# QUESTION 4
# ACCPET NAME AND AGE FROM THE USER AND CHECK WEATHER THE USER IS ELIGIBLE FOR VOTE OR NOT.

name = str(input("Enter your name:- "))
age = int (input("Enter the age also:- "))

if age>=18:
    print(f"{name} is eligible for vote ")
    print (f"{name} age is {age}")
else:
    print(f"{name} is NOT eligible ")
    print (f"{name} age is {age}")

# QUESTION 5
#  accpet any character and check it was a vowel or consonent


letter = input("Enter any letter to check ")
if letter in "aeiouAEIOU":
    print("This letter is a vowel")
else:
    print("It's not a vowel, it's a consonant")
