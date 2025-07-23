print("Welcome to the Love Calculator!")

name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()

# Combine names
combined_names = name1 + name2

# Count letters in "TRUE"
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
true_score = t + r + u + e

# Count letters in "LOVE"
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')  
love_score = l + o + v + e

# Final score
score = int(str(true_score) + str(love_score))

# Output result
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like Coke and Mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together .")
else:
    print(f"Your score is {score}.")
