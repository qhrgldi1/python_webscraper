from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

so_jobs = get_so_jobs() # StackOverflow Jobs Scrapping
indeed_jobs = get_indeed_jobs() # Indeed Jobs Scrapping
jobs = so_jobs + indeed_jobs # 둘을 합침

save_to_file(jobs)