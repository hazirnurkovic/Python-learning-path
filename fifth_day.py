# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
input_age = int(input("Enter your age: "))
print("You are old enough to drive") if input_age >= 18 else print(f"You have to wait {18 - input_age} years in order to be able to drive")

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age

my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    year = "years" if my_age - your_age > 1 else "year"
    print(f"I am {my_age - your_age} {year} older than you")
elif my_age < your_age:
    print("You are older than me")
else:
    print("We are the same age")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("a is greater than b") if a > b else print("a is smaller than b") if a < b else print("a is equal to b")

# Write a code which gives grade to students according to their scores:
# 80-100: A
# 70-79: B
# 60-69: C
# 50-59: D
# 0-49: F
score = int(input("Enter your score: "))
match score:
    case _ if score >= 80 and score <= 100:
        print("A")
    case _ if score >= 70 and score <= 79:
        print("B")
    case _ if score >= 60 and score <= 69:
        print("C")
    case _ if score >= 50 and score <= 59:
        print("D")
    case _ if score >= 0 and score <= 49:
        print("F")
    case _:
        print("Invalid score")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring

season = input("Enter a month: ")
match season:
    case _ if season in ["September", "October", "November"]:
        print("Autumn")
    case  _ if season in ["December", "January", "February"]:
        print("Winter")
    case  _ if season in ["March", "April", "May"]:
        print("Spring")
    case _:
        print("Invalid month")