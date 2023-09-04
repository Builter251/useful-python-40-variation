# 웹페이지 캡처 - 도서
from html2image import Html2Image

html = Html2Image()
html.screenshot(url="https://github.com/Builter251/useful-python-program-40-variation",save_as="builter-python-repo-safari.png")

# html2image 패키지로는 스크롤 캡처가 불가능(https://github.com/vgalin/html2image#faq)