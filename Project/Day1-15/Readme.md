#This is all project from Day01 - Day15
-------------------------------------------

Proeject List in order by Learning Day:

1. Tip Calculator
2. Treasure island
3. Rock Paper Scissor
4. Password Generator
5. Caesar
6. Blind Bidding System
7. Basic Calculator 
8. Blackjack
9. Number Guessing
10. Higher Lower


# Concepts Used in Day1 to Day 15


1 Basic Data Type:
-----------------------------------------
1. String
2. Integer 
3. Float 
4. Boolean : True/False

2 Conditional "IF" Statement
------------------------------------------
```
if condition:

	do this

else:

	do that
if true:

	#result would be false
```

condition = True

answer = input(”type ‘y’ or ‘n’ to change conditions.”)
```
if answer == "y":

	condition = True

if answer == "n":

	condition = False
```

#can convert to
```
if input(”type ‘y’ or ‘n’ to change condition.”) = n:

	condition = False
```
3 Nest "IF" Condition
---------------
```
if(xxxxxx):

	if(xxxxxx):

		do this

	else:

		do that

else:

	do that
```
4 Logical Operator
------------------------
A **and** B

C **or** D

**not** E

5 Random Module
-----------------------
import random
```
random.randint(a, b) = random int between a&b (including a&b)
random.random() = create a flout between 0.0 - 1.0
random.random() * 5 = 0-4.99999999
```
6 List Data Structure
--------------------------
1. Saving data in Python
2. variables = single data

List
```
fruit = [item1, item2]
print(fruit[0])
```

7 for Loop
-------------------
for "variable" in list
```
fruits = [”a”, “b”, “c”]
for fruit in fruits:
	print(fruit)

#output:
#a
#b
#c

```

8 Range
----------------
```
for number in range(1, 10) # = 1..2..3..4..5..6..7..8..9
for number in range(x, y, z) #x = largest, y = smallest, z step
```

9 Define Function
----------------
```
def my_function():
	print(”Hello”)
	print(”Bye”)

my_function()
```

10 While Loop
-----------------
```
While something is True/False:
```
How to Stop While Loop: Can use boolean to stop the repeatation
```
while **not** something:
```
**for loop VS while loop**

for loop have ending, while loop without ending unless the *condition* is changed.
