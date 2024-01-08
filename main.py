from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()  # 초기화

browser = p.chromium.launch(
    headless=False
)  # 크로미움 브라우저 실행. headless mode가 True라면 브라우저가 보이지 않는다.

page = browser.new_page()  # 브라우저 새창 열기

page.goto("https://www.wanted.co.kr/jobsfeed")  # 해당 url로 이동
time.sleep(5)

page.click("button.Aside_searchButton__Xhqq3")
time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(5)

page.keyboard.down("Enter")
time.sleep(5)

page.click("a#search_tab_position")
time.sleep(5)

for x in range(4):
    page.keyboard.down("End")
    time.sleep(5)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")
