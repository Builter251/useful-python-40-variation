"""
숫자 야구 게임 규칙
- 출제자는 0~9 사이의 중복되지 않은 숫자 3개를 정한다.
- 응시자는 한 번의 기회마다 3개의 숫자를 말한다.
    - 위치와 숫자 모두 일치하면 "스트라이크"
    - 숫자만 맞추고 위치는 일치하지 않으면 "볼"
    - 위치와 숫자 모두 틀리면 "아웃"
- 결과적으로, 응시자는 출체자가 제시한 숫자 3개를 위치와 숫자 모두 맞추면 된다.
"""

import random

def calc_game(user_nums, answer):
    strike, ball, out = 0, 0, 0
    for i in range(len(user_nums)):
        if user_nums[i] == answer[i]:
            strike += 1
        elif user_nums[i] in answer:
            ball += 1
        else:
            out += 1
    return strike, ball, out

numbers = list(range(0, 10))
answer = random.sample(numbers, 3)
print("정답:", answer)

inning = 1

while True:
    try:
        user_nums = list(map(int, input("0~9의 중복되지 않은 숫자 3개 입력: ").split()))

        if len(user_nums) != 3:
            print("3개의 숫자를 입력하십시오!")
        elif len(set(user_nums)) == 3:
            strike, ball, out = calc_game(user_nums, answer)
            print(f"{strike}S {ball}B {out}O")
            if user_nums == answer:
                print(f"게임 끝! {inning}번만에 맞췄습니다.")
                break
        inning += 1

    except ValueError:
        print("유효한 숫자를 입력하십시오!")



