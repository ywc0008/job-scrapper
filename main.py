from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()  # 초기화

browser = p.chromium.launch(
    headless=False
)  # 크로미움 브라우저 실행. headless mode가 True라면 브라우저가 보이지 않는다.

page = browser.new_page()  # 브라우저 새창 열기

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")  # 해당 url로 이동
time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")
# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# time.sleep(5)

# page.keyboard.down("Enter")
# time.sleep(5)

# page.click("a#search_tab_position")
# time.sleep(5)

for x in range(4):
    page.keyboard.down("End")
    time.sleep(5)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link,
    }
    jobs_db.append(job)


file = open("jobs.csv", "w")  # 파일 열여주는 명령어지만 파일이 없으면 만들어줌/ r은 읽기모드 w는 수정모드
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Location", "Reward", "Link"])
for job in jobs_db:
    writer.writerow(job.values())
file.close()
