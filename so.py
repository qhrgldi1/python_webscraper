import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

# stackovdflow의 마지막 page를 가져오는 함수
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True) # 마지막 페이지
    return int(last_pages)  # last_pages 변수를 range 함수에 쓰기 위해 integer로 변환

def extract_job(html):
    # title : 구인 제목, company : 회사명, location : 지역명
    title = html.find("a", {"class": "s-link"})["title"]
    company = html.find("h3", {"class": "fc-black-700"}).find("span").get_text(strip=True)
    location = html.find("span", {"class": "fc-black-500"}).get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    }

# 모든 페이지의 직업 set(title, company, location)를 추출하여 jobs 리스트에 저장
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs

# 직업 공고를 가져오는 함수
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs