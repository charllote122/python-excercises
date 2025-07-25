numbers_input = input("Enter the numbers separated by space: ")
numbers_list = numbers_input.split()

maximum = int(numbers_list[0])

for i in range(1, len(numbers_list)):
    num = int(numbers_list[i])
    if num > maximum:
        maximum = num

print("Maximum number is:", maximum)
