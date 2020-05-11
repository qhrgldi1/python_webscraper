import requests
from bs4 import BeautifulSoup

# 페이지를 넘길 때 마다 바뀌는 인자 : LIMIT
LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# Indeed 웹사이트의 page를 추출하기 위한 함수 정의
def extract_indeed_pages():
    # html 가져오기 위한 라이브러리
    result = requests.get(URL)

    # soup 생성, result 페이지의 html 추출
    soup = BeautifulSoup(result.text, "html.parser")

    # find : 태그값을 기준으로 내용 불러오기(최초 검색 결과만 출력)
    pagination = soup.find("div", {"class":"pagination"})

    # 해당 모든 태그를 불러옴(리스트 형식)
    links = pagination.find_all("a")

    # 빈 list 생성
    pages = []

    # span 태그를 pages 리스트에 추가함 (for)
    # 마지막 요소인 "next..."를 제외하기 위해 links의 슬라이싱을 지정
    for link in links[:-1]:
        # anchor 태그(links) 안에 있는 text만 가져오기 (string)
        pages.append(int(link.string))

    # 마지막 페이지 반환
    max_page = pages[-1]
    return max_page

# 마지막 페이지까지 잘 동작하는지 확인하는 함수
def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")

    # 직업 공고를 가져오기 위한 soup 준비
    soup = BeautifulSoup(result.text, "html.parser")

    # 직업 공고의 div 클래스를 모두 가져옴 -> results에 저장(리스트)
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

    # h2 title 태그를 모두 가져옴
    for result in results:
        '''
        먼저 h2태그의 title class를 가져온 후
        title 안의 anchor의 attribute title(공고 제목)을 가져옴
        '''
        title = result.find("h2", {"class":"title"}).find("a")["title"]
        print(title)
    return jobs
