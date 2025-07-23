weight = float(input("Enter your weight: "))
unit = input("Is this in (K)g or (L)b? ").lower()

if unit in ['k', 'kg']:
    converted = weight * 2.20462
    print(f"{weight} kg is {round(converted, 2)} pounds.")
elif unit in ['l', 'lb']:
    converted = weight / 2.20462
    print(f"{weight} lb is {round(converted, 2)} kilograms.")
else:
    print("Invalid unit! Please enter 'K', 'KG', 'L', or 'LB'.")
