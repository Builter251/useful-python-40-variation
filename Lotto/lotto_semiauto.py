# 로또 반자동 입력
"""
사용자 입력
랜덤 생성
사용자 입력 + 랜덤 생성
---
6개 다 입력해도 상관 없고
아무것도 입력안해도 전부 랜덤
일부만 입력해도 나머지는 랜덤
"""
import random

MAX_SELECTION = 6
NUMBER_RANGE = range(1,46)

random.seed()

# 진행할 게임 수 검증
while True:
    try:
        number_of_games = int(input("진행할 게임수를 (1게임 이상): "))
        if number_of_games >= 1 :
            break
        else:
            print("게임은 최소 1게임 이상 진행되어야 합니다.")
    except ValueError:
        print("생성 게임수를 1 이상 정수로 입력하십시오.")

def generate_lotto_numbers(user_numbers):
    random_numbers = [num for num in NUMBER_RANGE if num not in user_numbers]
    selected_random = random.sample(random_numbers, MAX_SELECTION - len(user_numbers))
    
    lotto_numbers = user_numbers + selected_random
    lotto_numbers.sort()
    
    return lotto_numbers

def main():
    for i in range(number_of_games):
        while True:
            try:    
                user_input = input(f"반자동 {i+1}게임 숫자 입력 (공백 구분)")          
                user_numbers = list(map(int,user_input.split()))               
                num_selected = len(user_numbers)

                if num_selected > MAX_SELECTION:
                    print("6개 이하 숫자를 입력하세요")
                    continue

                if not all(1 <= num <= 45 for num in user_numbers):
                    print("1에서 45사이의 숫자만 입력하세요.")
                    continue
                
                lotto_numbers = generate_lotto_numbers(user_numbers)

                print(f"{1+i}게임 로또 번호: {lotto_numbers}")
                break
            except ValueError:
                print("정수를 입력하세요")

if __name__ == "__main__":
    main()