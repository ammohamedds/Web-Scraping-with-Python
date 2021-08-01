from bs4 import BeautifulSoup
import requests
import time

# we will filter based on input
print('Please enter required skills')
required_skills = input('>')
print(f'The required skill is {required_skills}')


def get_job():
        #html_text1 = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')
        html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
        # print(html_text1)
        # print(html_text)
        # Create Instance
        soup = BeautifulSoup(html_text, 'lxml')
        # type(soup)
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        # print(job)
        for index, job in enumerate(jobs):
            # We need to select just few jobs or Posted
            published_date = soup.find('span', class_='sim-posted').text
            # print(published_date)
            if 'Posted' in published_date:  # i can select few days
                # company_name = soup.find('h3', class_='joblist-comp-name').text.strip(' ')
                company_name = soup.find('h3', class_='joblist-comp-name').text.replace(' ', '')
                skills = soup.find('span', class_='srp-skills').text.replace(' ', '')
                # print(company_name)
                job_description = job.header.h2.a['href']
                if required_skills in skills:  # we will filter based on input
                   with open(f'post/{index}.txt', 'w') as f: # please create fold names post before this step
                        # create and name file for  each post
                        # W for writing , so we will replace print with write
                        f.write(f'Company name:{company_name.strip()} \nRequired skills:{skills.strip()}\n')
                        # print('Company name:{} and Required skills:{}.'.format(company_name,skills))
                        f.write(f'published_date:{published_date.strip()}\n')
                        # if we need job description, we go to header, then h2 then a tag
                        f.write(f'Job Description:{job_description}')
                print(f'File is saved{index}')


if __name__ == '__main__':
      while True:
            get_job()
            wait_time = 50
            print(f'Waiting {wait_time} Seconds...')
            time.sleep(wait_time * 1)  # multiply by 60 if u want to change to minute and this is better
