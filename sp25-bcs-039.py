# Activity 1
print("Activity 1")

x = 4
if(x == 3):
    print("Lions are king of the Jungle")
if(x == 4 ):
    print("Bears eat Honey")

print("\n**************************************\n")

# Activity 2
print("Activity 2")

x = 4
if(x == 3):
    print("Lions are king of the Jungle")
else:
    print("Bears eat Honey")

print("\n**************************************\n")

# Activity 3
print("Activity 3")

x = 4
if(x == 3):
    print("Lions are the kingd of the Jungle")
elif(x == 4):
    print("Canberra is the capital of Australia")
else:
    print("Bera eat Honey")

print("\n**************************************\n")

# Activity 4
print("Activity 4")

x = int(input("Enter x : "))
y = int(input("Enter y : "))

if(x <= 2 and y < 20):
    print("The numbers x and y fall under the category")
    sum = x + y
    if(sum < 50):
        print("The sum of x and y is ",sum)
else:
    print("The numbers x and y do not fall under the category")

print("\n**************************************\n")

# Activity 5
print("Activity 5")

year = int(input("Enter year : "))
zodiacYear = year % 12
if(zodiacYear == 0):
    print("Monkey")
elif(zodiacYear == 1):
    print("Rooster")
elif(zodiacYear == 2):
    print("Dog")
elif(zodiacYear == 3):
    print("Pig")
elif(zodiacYear == 4):
    print("Rat")
elif(zodiacYear == 5):
    print("Ox")
elif(zodiacYear == 6):
    print("Tiger")
elif(zodiacYear == 7):
    print("Rabit")
elif(zodiacYear == 8):
    print("Dragon")
elif(zodiacYear == 9):
    print("Snake")
elif(zodiacYear == 10):
    print("Horse")
else:
    print("Sheep")

print("\n**************************************\n")

# Lab Task 1
print("Lab Task 1")

x = int(input("Enter an integar : "))
if(x == 0):
    print("Number entered id Zero")
elif(x < 0):
    print("Number entered is negative / less than zero")
else:
    print("Number is positive / greater than zero")

print("\n**************************************\n")

# Lab Task 2
print("Lab Task 2")

marks1 = float(input("Enter Physics Marks (? / 100) : "))
marks2 = float(input("Enter Chemistry Marks (? / 100) : "))
marks3 = float(input("Enter Biology Marks (? / 100) : "))
marks4 = float(input("Enter Mathematics Marks (? / 100) : "))
marks5 = float(input("Enter Computer Marks (? / 100) : "))

percentage = ((marks1 + marks2 + marks3 + marks4 + marks5) / 500 * 100)

if(percentage >= 90):
    print("Grade A")
elif(percentage >= 80):
    print("Grade B")
elif(percentage >= 70):
    print("Grade C")
elif(percentage >= 60):
    print("Grade D")
elif(percentage >= 40):
    print("Grade E")
else:
    print("Grade F")

print("\n**************************************\n")


# Lab Task 3
print("Lab Task 3")

side1 = float(input("Enter side 1 of triangle : "))
side2 = float(input("Enter side 2 of triangle : "))
side3 = float(input("Enter side 3 of triangle : "))

if(side1 == side2 and side1 == side3 and side2 == side3):
    print("Equilateral Triangle")
elif(side1 == side2) or (side1 == side3) or (side2 == side3):
    print("Iscoceles Triangle")
else:
    print("Scalenne Triangle")

print("\n**************************************\n")


# Lab Task 4
print("Lab Task 4")

year = int(input("Enter year : "))

if(year % 4 == 0 or year % 400 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    ("Not a leap year")

print("\n**************************************\n")

# Lab Task 5
print("Lab Task 5")

correct_username = "aneebazmat32@gmail.com"
correct_password = "aneeb039"
isCorrect = False

while(not isCorrect):
    username = input("Enter UserName : ")
    password = input("Enter password : ")

    if(username == correct_username and password == correct_password):
        isCorrect = True

    elif(username == correct_username):
        while(password != correct_password):
            password = input("Incorrect password.Enter password Again : ")

    elif(password == correct_password):
        while(username != correct_username):
            print("Incorrect userName.Enter username Again")

    else:
        print("Username and password are incorrect")

    print("\n**************************************\n")
