from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_compoenets():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"      # assert: 강하게 주장하다, 실력을 행사하다

    driver.implicitly_wait(0.5)     # implicity: 함축, 내재

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()

print("END")