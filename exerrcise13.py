row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

map = [row1, row2, row3]

# Show the initial grid
print(f"{row1}\n{row2}\n{row3}")

# Ask the user where to hide the money
position = input("Enter the position to hide the money (e.g., 23 = row 2, column 3): ")

# Convert input to index
row_number = int(position[0]) - 1   # subtract 1 to get 0-based index,,this is because list starts at index 0 not 1.
column_number = int(position[1]) - 1

# Replace the selected position with a symbol (e.g., "$")
map[row_number][column_number] = "$"

# Show the updated grid
print(f"{row1}\n{row2}\n{row3}")
