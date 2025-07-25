numbers = [1, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        break # If an even number is found, exit the loop
else:
    print("No even number found.")
