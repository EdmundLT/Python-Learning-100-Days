"""
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
"""

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_given = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

tip_given = 1 + tip_given / 100
each_pay = round(total_bill / people * tip_given, 3)
print(f"Each person should pay: {each_pay}")
