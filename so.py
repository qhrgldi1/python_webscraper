import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

# stackovdflow의 page를 가져오는 함수
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pages)


# 직업 공고를 가져오는 함수
def get_jobs():
    last_page = get_last_page()
    return []