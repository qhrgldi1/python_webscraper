# indeed.py에서 정의된 함수를 가져옴
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

# indeed 웹 스크래퍼 완성
# indeed_jobs = get_indeed_jobs()
# print(indeed_jobs)

# StackOverflow
so_jobs = get_so_jobs()