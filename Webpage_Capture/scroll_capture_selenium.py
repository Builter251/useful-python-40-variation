from selenium import webdriver
import time

# Chrome 브라우저 시작
driver = webdriver.Chrome()

# 캡처할 웹 페이지 열기
url = 'https://www.naver.com'
driver.get(url)

# 웹 페이지 로딩을 위해 충분한 시간 기다리기 (필요에 따라 조절)
time.sleep(5)

# 페이지 높이 구하기
page_height = driver.execute_script("return document.documentElement.scrollHeight")

# 브라우저 높이만큼 스크롤하며 스크린샷 찍기
screenshot_count = 0

while True:
    # 스크린샷 찍기
    screenshot_path = f"./screenshots/screenshot_{screenshot_count}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot: {screenshot_path}")
    
    # 페이지 아래로 스크롤
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    
    # 스크롤 후 로딩을 위해 충분한 시간 기다리기 (필요에 따라 조절)
    time.sleep(5)
    
    # 현재 스크롤 위치 확인
    current_scroll = driver.execute_script("return window.pageYOffset;")
    
    # 전체 페이지를 다 스크롤한 경우 종료
    if current_scroll-1 >= page_height:
        break
    
    screenshot_count += 1

# Chrome 브라우저 종료
driver.quit()
