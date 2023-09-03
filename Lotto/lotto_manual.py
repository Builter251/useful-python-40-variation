#로또 수동 입력 - 완료

MAX_SELECTION = 6
games = []

while True:
    try:
        number_of_games = int(input("생성 게임수: "))
        if number_of_games >= 1:
            break
        else:
            print("최소 게임수는 1 이상입니다.")
    except ValueError:
        print("생성 게임수를 정수로 입력하십시오.")

def verify_input(single_game):
    try:
        single_game_nums = list(map(int,single_game))
        if len(single_game_nums) != MAX_SELECTION:
            return "6개의 숫자를 입력하세요."
        if not all(1 <= num <= 45 for num in single_game_nums):
            return "1에서 45사이의 숫자만 입력하세요"
        if len(single_game_nums) != len(set(single_game_nums)):
            return "중복되지 않은 숫자를 입력하세요"
        return sorted(single_game_nums)
    except ValueError:
        return "정수를 입력하세요"

for i in range(number_of_games):
    while True:
        single_game_input = input(f"{i+1}게임 입력 (공백 구분): ")
        single_game_splited = single_game_input.split()
        verified_nums = verify_input(single_game_splited)
        
        if isinstance(verified_nums, list):
            games.append(verified_nums)
            break
        else:
            print(verified_nums)

print(games)
