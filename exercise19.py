max_jump = int(input("Enter your maximum jump height: "))
hurdles = input("Enter the hurdle heights separated by spaces: ").split()

i = 0
max_hurdle = int(hurdles[0])

while i < len(hurdles):
    height = int(hurdles[i])
    if height > max_hurdle:
        max_hurdle = height
    i += 1

need = max_hurdle - max_jump
if need > 0:
    print(need)
else:
    print(0)
