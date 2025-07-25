numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        break
else:
    print("No even number found.")
