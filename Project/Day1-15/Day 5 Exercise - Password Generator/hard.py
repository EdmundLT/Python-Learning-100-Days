# Password Generator Project
import random
import xdrlib
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele
    
    return str1


pw = []
password_hard = ""
total_digit = int(nr_letters + nr_numbers + nr_symbols)
for x in range(nr_letters):
    pw.append(random.choice(letters))
for x in range(nr_symbols):
    pw.append(random.choice(symbols))
for x in range(nr_numbers):
    pw.append(random.choice(numbers))
random.shuffle(pw)
print(listToString(pw))
