import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

# stackovdflow의 마지막 page를 가져오는 함수
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-3].get_text(strip=True)
    return int(last_pages)  # last_pages 변수를 range 함수에 쓰기 위해 integer로 변환

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})

        # 공고별로 부여된 jobid 가져오기
        for result in results:
            print(result["data-jobid"])

# 직업 공고를 가져오는 함수
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs 