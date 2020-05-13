import requests
from bs4 import BeautifulSoup

# 페이지를 넘길 때 마다 바뀌는 인자 : LIMIT
LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# Indeed 웹사이트의 page를 추출하기 위한 함수 정의
def get_last_page():
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

# indeed 각 페이지의 직업, 회사명, 지역을 추출하는 함수
def extract_job(html):
    '''
    먼저 h2태그의 title class를 가져온 후
    title 안의 anchor의 attribute title(공고 제목)을 가져옴
    '''
    title = html.find("h2", {"class":"title"}).find("a")["title"]
    
    # 회사명 가져오기
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    
    # 회사명이 anchor로 지정되어 있다면 if, 아니면 else
    # 출력 결과 빈칸이 많아 str로 형변환
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)

    # 양 끝의 공백을 없애는 strip
    company = company.strip()

    # 지역명 가져오기
    # div 클래스에서 display: none 항목이 있어 None인 지역명이 있기 때문에
    # Attribute로 가져옴
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]

    # Apply 링크를 가져오기 위한 URL안의 ID 가져오기
    job_id = html["data-jk"]

    return {
        'title': title, 
        'company': company, 
        'location': location, 
        'link': f"https://www.indeed.com/viewjob?jk={job_id}"
    }


# extract_job 함수에서 받은 정보를 jobs 리스트에 저장하여 return 하는 함수
def extract_jobs(last_page):
    # 직업과 회사명 dictionary를 추가할 'jobs' list 생성
    jobs = []

    for page in range(last_page):
        # 페이지 세기 위한 print
        print(f"Scrapping Indeed: Page: {page}")

        result = requests.get(f"{URL}&start={page*LIMIT}")

        # 직업 공고를 가져오기 위한 soup 준비
        soup = BeautifulSoup(result.text, "html.parser")

        # 직업 공고의 div 클래스를 모두 가져옴 -> results에 저장(리스트)
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

        # 직업과 회사명을 출력하는 부분을 extract_job으로 따로 함수 생성
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    # 마지막 페이지 return : get_last_page
    last_page = get_last_page()

    # 마지막 페이지를 인자로 받아 채용 공고 Scrapper (채용 제목, 회사명, 지역명, apply url)
    jobs = extract_jobs(last_page)
    return jobs
