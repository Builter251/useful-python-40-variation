from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import datetime

start = time.time()

# headless 모드?
# https://stackoverflow.com/questions/53083952/difference-of-headless-browsers-for-automation
# timeout 방지
# https://stackoverflow.com/questions/61254755/selenium-timeout-exception-on-save-screenshot-on-very-large-windows
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--force-device-scale-factor=1')

driver = webdriver.Chrome(options=chrome_options)
page = 'https://www.apple.com/kr/iphone/compare/?modelList=iphone-14-pro,iphone-15,iphone-15-pro'
driver.get(page)

# 웹 화면의 너비/높이 정리
# https://jsfiddle.net/y8Y32/25/
# https://ko.javascript.info/size-and-scroll-window
page_height = driver.execute_script('return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight,document.body.offsetHeight, document.documentElement.offsetHeight, document.body.clientHeight, document.documentElement.clientHeight);')
page_width = 1920
# page_width  = driver.execute_script('return document.documentElement.scrollWidth;')
driver.set_window_size(page_width,page_height)
print('page_width: ', page_width)
print('page_height: ', page_height)

suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
file_name = suffix + '.png'

# selenium 시간 대기 차이
# https://semo-info.com/entry/selenium-implicit-explicit
time.sleep(10)

try:
    driver.save_screenshot(file_name)
except TimeoutException:
    print("Timeout Occurred")
    pass

driver.quit()
end = time.time()

sec = (end - start)
runtime = datetime.timedelta(seconds=sec)
print('runtime: ', runtime)