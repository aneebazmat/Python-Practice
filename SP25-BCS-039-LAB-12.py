# Activity : 1
print()
print("Activity : 1")
print("Python program to tell the number of characters in a string. ") 
x = "This is Python"
print("The Length of x =",len(x))
print("The value of x is : ", 2)
print("The value of x is : ", 3)

print("\n*****************************\n")

# Activity : 2
print("Activity : 2")
print("Python program to illustrate using a string with escaped characters.")
x = "\"This is Python\",said Amanda"
print(x)
y = "\"This is Java\", my brother"
print(y)

print("\n*****************************\n")

# Activity : 3
print("Activity : 3")
print("Python program to illustrate string concatenation, indexing, and slicing.")
string1 = "Pakistan"
string2 = "India is a 2nd largest asian country whose order has been Postponed"
result = string1 + " vs " + string2[:5] + " match " + string2[11] + " " + string2[58:]
print(result)


print("\n*****************************\n")

# Activity : 4
print("Activity : 4")
print("Python program to illustrate membership testing .")
string = input("Enter a string : ")
if "Python" in string:
    print ("Python","is in",string)
else:
    print("Python is not in",string)


print("\n*****************************\n")

# Activity : 5
print("Activity : 5")
string = input("Enter a string : ")
string = string.strip()                       # Remove the white spaces in a string for comparison

start = 0                                     # Index of first character in a string
end = len(string) - 1                         # Index of last character in a string

while (start < end):                          # While Loop for repetition
    if (string[start] == string[end]):
        start += 1
        end -= 1
    else:
        print("Not Palindrome")
        break

if (start == end):
    print("It's a Palindrome")

print("\n*****************************\n")

# Activity : 6
print("Activity : 6")

string = "welcome to python"
string = string.capitalize()
print(string)
string = string.title()
print(string)
string = string.upper()
print(string)
string1 = "WELCOME PAKISTAN"
string1 = string1.lower()
print(string1)
string2 = "wELCOME TO lAHORE"
string2 = string2.swapcase()
print(string2)
string3 = "New England"
string3 = string3.replace("England","Pakistan")
print(string3)

print("\n*****************************\n")

# Lab Task 1
print("Lab Task : 1")
print("The python program to swap first word with z. ")
string = input("Enter a string : ")

if(len(string) > 0):
    new_string = "Z" + string[1:]
    print("Modified String :",new_string)
else:
    print("You have entered an empty string")

print("\n*****************************\n")

# Lab Task 2
print("Lab Task : 2")
print("Python program to print only odd characters.")
string = input("Enter a string: ")

# Characters at even indices (0, 2, 4, ...)
Result = string[::2]                                      # string[start:stop:step]   step = 2
print("Modified string (odd indices removed):", Result)

print("\n*****************************\n")

# Lab Task 3
print("Lab Task : 3")
print("Python program for concatenation of two strings.")
string_1 = input("Enter a string 1 : ")
string_2 = input("Enter a string 2 : ")

if(len(string1) >= 2 and len(string_2) >= 2 ):
    new_string_1 = string_2[:2] + string_1[2:]
    new_string_2 = string_1[:2] + string_2[2:]

    Result = new_string_1 + " " + new_string_2

print("After Concatenation and Swapping:",Result)

print("\n*****************************\n")

# Lab Task 4
print("Lab Task : 4")
print("Python program to remove characters at 0,4 and 5 position. ")
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("The enterned list is : ", my_list)
new_list = [item for index, item in enumerate(my_list) if index not in (0, 4, 5)]
print("The new updated list:", new_list)

print ("****************** Thanks *************************")

 

