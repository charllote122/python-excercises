print("Welcome to Python Pizza!")

size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

# Pizza price
if size == "S":
    bill += 100
if size == "M":
    bill += 200
if size == "L":
    bill += 300

# Pepperoni price
if add_pepperoni == "Y":
    if size == "S":
        bill += 30
    else:
        bill += 50

# Extra cheese price
if extra_cheese == "Y":
    bill += 20

print(f"Your final bill is: Ksh {bill}")
