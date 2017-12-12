import requests
from bs4 import BeautifulSoup


url = 'https://stackoverflow.com/jobs?sort=i&q=python'
response = requests.get(url)
html = response.content
print(html)

soup = BeautifulSoup(html)

results = soup.find('div', attrs={'class': 'listResults'})

list_titles = []
list_companies = []
for job in results.findAll('div', attrs={'class': '-job-summary'}):
    title_div = job.find('div', attrs={'class': '-title'})
    job_title = title_div.find('a', attrs={'class': 'job-link'})
    list_titles.append(job_title.string)
    company_div = job.find('div', attrs={'class': '-company'})
    print(job.prettify())
    print(list_titles)