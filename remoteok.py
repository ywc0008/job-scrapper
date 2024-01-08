import requests
from bs4 import BeautifulSoup

all_jobs = []
keywords = ["python", "golang", "javascript"]


def scrape_page(keyword):
    print("Scraping...")
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        },
    )
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        region = job.find("div", class_="location").text
        job_data = {"title": title, "company": company, "region": region}
        all_jobs.append(job_data)


for keyword in keywords:
    scrape_page(keyword)

print(all_jobs)
