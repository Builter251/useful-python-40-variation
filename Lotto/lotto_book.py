import random

numbers = list(range(1,46))
# print(numbers)

selected_numbers = random.sample(numbers, 6)
selected_numbers.sort()
print(selected_numbers)