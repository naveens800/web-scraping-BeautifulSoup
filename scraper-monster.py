import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL).text

soup = BeautifulSoup(page,'html.parser')

#find element by id
results = soup.find(id = "SearchResults")
print("total search results",len(results))
# print(results.prettify())

#find element by classname
job_elems = results.find_all('section',class_ = "card-content")
print("total job postings", len(job_elems))
none = 0


#find title, company name, location_elem in each job_elem
for job_elem in job_elems:
    title_elem = job_elem.find('h2',class_ = 'title')
    company_elem = job_elem.find('div',class_="company")
    location_elem = job_elem.find('div',class_ = "location")
    if None in (title_elem,company_elem,location_elem):
        none+=1
        continue
    # print(title_elem.text.strip())
    # print(company_elem.text.strip())
    # print(location_elem.text.strip())
    # print('--------------------------------------------------------')

#find specific technical job posting's
technical_jobs = results.find_all('h2',string = lambda text: ('technical' or 'software'or 'lead') in text.lower())


#find 'apply' links of tech job postings
for tech_job in technical_jobs:
    link = tech_job.find('a')['href']
    print(tech_job.text.strip())
    print(f'Apply here: {link}\n')

