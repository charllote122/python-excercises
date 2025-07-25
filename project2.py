import random
import string

letters = list(string.ascii_letters)  # a-z + A-Z
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = list(string.digits)         # 0-9

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)


password = ''.join(password_list)
print(f"Your generated password is: {password}")
