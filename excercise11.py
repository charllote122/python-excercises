fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = ["text", 99, 3.14, True, [1, 2]]

# Accessing values
print(fruits[0])         
print(fruits[1:3])       
print(mixed)

# Modifying list
fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("banana")
fruits.pop()
more_fruits = ["kiwi", "pineapple"]
fruits.extend(more_fruits)

# Sorting and reversing
numbers.sort()
numbers.reverse()

# Inbuilt functions
print(min(numbers))      
print(max(numbers))      
