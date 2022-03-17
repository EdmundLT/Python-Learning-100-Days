
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_given = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

tip_given = 1 + tip_given / 100
each_pay = round(total_bill / people * tip_given, 3)
print(f"Each person should pay: {each_pay}")
