import requests

# html 가져오기 위한 라이브러리
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# html 출력
print(indeed_result.text)