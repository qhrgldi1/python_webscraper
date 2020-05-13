import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", newline="" ,encoding='UTF-8') # 쓰기 모드
    writer = csv.writer(file)
    # csv의 첫 줄(row) 작성
    writer.writerow(["title", "company", "location", "link"])
    
    for job in jobs:
        writer.writerow(list(job.values()))
    return