heights_input = input("Enter the heights separated by space: ")
heights_list = heights_input.split()

total_height = 0
count = 0

for i in range(len(heights_list)):
    height = int(heights_list[i])  # Convert to int
    total_height += height
    count += 1

average_height = total_height / count

print("Average height is:", round(average_height, 2))
