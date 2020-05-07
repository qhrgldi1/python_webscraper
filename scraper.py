import requests
from bs4 import BeautifulSoup

# html 가져오기 위한 라이브러리
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

'''
# html 전체 출력
print(indeed_result.text)
'''

# soup 생성, indeed_result 페이지의 html 추출
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# find : 태그값을 기준으로 내용 불러오기(최초 검색 결과만 출력)
pagination = indeed_soup.find("div", {"class":"pagination"})

# 해당 모든 태그를 불러옴(리스트 형식)
pages = pagination.find_all("a")

# 빈 list 생성
spans = []

# span 태그를 spans 리스트에 추가함 (for)
for page in pages:
    spans.append(page.find("span"))

# 마지막 리스트 요소를 제외하고 출력
print(spans[:-1])