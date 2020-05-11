# indeed.py에서 정의된 함수를 가져옴
from indeed import extract_indeed_pages, extract_indeed_jobs

# 마지막 페이지 return : last_indeed_pages
last_indeed_pages = extract_indeed_pages()

# 마지막 페이지를 인자로 받아 정상적으로 동작하는지 확인하는 함수
indeed_jobs = extract_indeed_jobs(last_indeed_pages)

print(indeed_jobs)