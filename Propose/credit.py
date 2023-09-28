import pygame
import sys

# pygame 초기화
pygame.init()

# 화면 설정
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Movie Credits')

# 시스템 폰트 리스트
# for i in pygame.font.get_fonts():
#     print(i)

# 글꼴 설정
font = pygame.font.SysFont("d2codingver13220180524all", 15)

# 크레딧 텍스트
# lines = [
#     "Producer: Your Name",
#     "Director: Director Name",
#     "Writer: Writer Name",
#     "Starring: Actor 1, Actor 2, Actor 3",
#     "Cinematographer: Cinematographer Name",
#     "Music: Composer Name",
# ]

# 텍스트 파일 읽기
with open("LoremIpsum.txt", "r") as f:
    lines = f.readlines()

# f = open("LoremIpsum.txt", "r")
# lines = f.readlines()
# for line in lines:
#     line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
#     print(line)
# f.close()

# 텍스트 위치 설정
text_x = screen_width
text_y = screen_height

# 텍스트 이동 속도 설정
text_speed = 1.5

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 검은색으로 채우기
    screen.fill((0, 0, 0))

    # 각 크레딧 텍스트를 표시하고 이동시키기
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, text_y + i * 50)
        screen.blit(text_surface, text_rect)

    text_y -= text_speed

    # 텍스트가 화면 밖으로 벗어나면 종료
    if text_y < -len(lines) * 50:
        running = False
        # text_y = screen_height

    pygame.display.flip()
    pygame.time.delay(20)

# pygame 종료
pygame.quit()
sys.exit()
