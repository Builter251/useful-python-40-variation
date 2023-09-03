# 로또 자동 입력

import random

numbers = list(range(1, 46))
random.seed()

while True:
    try:
        number_of_games = int(input("생성할 게임 수를 입력하세요 >> "))
        if number_of_games <= 0:
            pass
        else:
            break
    except ValueError:
        pass

for i in range(1, number_of_games + 1):
    selected_numbers = random.sample(numbers, 6)
    selected_numbers.sort()
    print(f"{str(i)}게임: {selected_numbers}")