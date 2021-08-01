from bs4 import BeautifulSoup
import requests

# we will filter based on input
print('Please enter required skills')
required_skills = input('>')
print(f'The required skill is {required_skills}')

def find_jobs():
    html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    # print(html_text1)
    # print(html_text)
    # Create Instance
    soup = BeautifulSoup(html_text, 'lxml')
    # type(soup)
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(job)
    for job in jobs:
        # We need to select sqljust few jobs or Posted
        published_date = soup.find('span', class_='sim-posted').text
        # print(published_date)
        if 'Posted' in published_date:  # i can select few days
            # company_name = soup.find('h3', class_='joblist-comp-name').text.strip(' ')
            company_name = soup.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = soup.find('span', class_='srp-skills').text.replace(' ', '')
            # print(company_name)
            job_description = job.header.h2.a['href']
            if required_skills in skills:  # we will filter based on input
                print(f'Company name:{company_name.strip()} \nRequired skills:{skills.strip()}')
                # print('Company name:{} and Required skills:{}.'.format(company_name,skills))
                print(f'published_date:{published_date.strip()}')
                # if we need job description, we go to header, then h2 then a tag
                print(f'Job Description:{job_description}')



find_jobs()