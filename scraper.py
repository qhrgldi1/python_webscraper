import requests
from bs4 import BeautifulSoup

# html 가져오기 위한 라이브러리
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# soup 생성, indeed_result 페이지의 html 추출
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# find : 태그값을 기준으로 내용 불러오기(최초 검색 결과만 출력)
pagination = indeed_soup.find("div", {"class":"pagination"})

# 해당 모든 태그를 불러옴(리스트 형식)
links = pagination.find_all("a")

# 빈 list 생성
pages = []

# span 태그를 pages 리스트에 추가함 (for)
# 마지막 요소인 "next..."를 제외하기 위해 links의 슬라이싱을 지정
for link in links[:-1]:
    # anchor 태그(links) 안에 있는 text만 가져오기 (string)
    pages.append(int(link.string))

# 마지막 페이지
max_page = pages[-1]