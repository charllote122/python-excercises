def hurdle_race(k, height):
    tallest = height[0]
    for h in height:
        if h > tallest:
            tallest = h
    extra_needed = tallest - k
    return max(0, extra_needed)

k = int(input("Enter your maximum jump height: "))
height_input = input("Enter the hurdle heights separated by spaces: ")
height = list(map(int, height_input.split()))
print(hurdle_race(k, height))
