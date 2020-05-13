# indeed.py에서 정의된 함수를 가져옴
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

so_jobs = get_so_jobs() # StackOverflow Jobs Scrapping
indeed_jobs = get_indeed_jobs() # Indeed Jobs Scrapping
jobs = so_jobs + indeed_jobs # 둘을 합침

print(jobs)