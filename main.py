from playwright.sync_api import sync_playwright
import time

p = sync_playwright().start()  # 초기화

browser = p.chromium.launch(
    headless=False
)  # 크로미움 브라우저 실행. headless mode가 True라면 브라우저가 보이지 않는다.

page = browser.new_page()  # 브라우저 새창 열기

page.goto("https://www.wanted.co.kr/jobsfeed")  # 해당 url로 이동

time.sleep(7)

page.screenshot(path="screenshot.png")  # 페이지 스크린샷 찍기
