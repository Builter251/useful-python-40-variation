from selenium import webdriver
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 캡처할 웹 페이지 열기
screenshot_count = 0
url = "https://www.naver.com"  # 캡처할 페이지 URL 입력
driver.get(url)
time.sleep(5)  # 페이지가 로드될 때까지 대기

# 스크롤 루프 시작
while True:
    # 웹 페이지의 필요한 요소를 선택
    
    # 자바스크립트 실행하여 스크롤 정보 가져오기
    scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")
    scroll_top = driver.execute_script("return document.documentElement.scrollTop;")
    client_height = driver.execute_script("return document.documentElement.clientHeight;")
    
    
    screenshot_path = f"/Webpage_Capture/screenshot_{screenshot_count}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot: {screenshot_path}")
    screenshot_count += 1

    # 스크롤이 페이지 끝까지 도달하면 루프 종료
    if scroll_height - scroll_top == client_height:
        break

    # 스크롤 다운
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(5)  # 스크롤 후 대기

# 웹 드라이버 종료
driver.quit()