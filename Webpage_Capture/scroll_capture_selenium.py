# Selenium으로 현재 보이는 창(Client Height) 만큼 캡처

from selenium import webdriver
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 캡처할 웹 페이지 열기
screenshot_count = 0
driver.maximize_window()
url = "https://www.apple.com/macbook-pro-13/"  # 캡처할 페이지 URL 입력
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


##################################################################

# 개발자 도구 명령어 "원본 크기 스크린샷 캡처" 로 스크롤 캡처 시도 - 실패
"""
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# # 크롬 드라이버 실행
# driver = webdriver.Chrome()

# # 웹 페이지 열기
# driver.maximize_window()
# driver.get('https://www.daum.net')
# ActionChains(driver)\
#         .send_keys(Keys.F12)\
#         .perform()

# time.sleep(5)

# # 명령 팔레트 열기
# ActionChains(driver).key_down(Keys.COMMAND).key_down(Keys.SHIFT).send_keys('P').key_up(Keys.COMMAND).key_up(Keys.SHIFT).perform()


# # 명령 팔레트에 원본 크기 스크린샷 명령 입력 후 엔터
# ActionChains(driver).send_keys('원본 크기 스크린샷 캡처').send_keys('\n').perform()

# # 스크린샷을 캡처하는 데 시간이 걸릴 수 있으므로 충분히 기다립니다.
# time.sleep(5)

# # 브라우저 종료
# driver.quit()
"""
