"""Scrape Stack Overflow job listings."""
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import os


def scrape_page(url):
    """Get URL and use BeautifulSoup to filter out job postings."""
    unflitered_jobs = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find('div', attrs={'class': 'listResults'})
    for job in results.findAll('div', attrs={'class': '-job-summary'}):
        unflitered_jobs.append(job)
    organize_results(unflitered_jobs)


def organize_results(results):
    """Function to filter all categories and write to CSV file."""
    if os.stat("jobs.csv").st_size != 0:
        f = open('jobs.csv', "w+")
        f.close()
    with open('jobs.csv', 'a') as csvfile:
        fieldnames = ['date', 'link', 'title', 'posted', 'company', 'location', 'tags']
        create = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='$')
        for post in results:
            create.writerow({
                'date': datetime.datetime.now(),
                'link': filter_title(post)[0],
                'title': filter_title(post)[1],
                'posted': filter_time(post),
                'company': filter_company(post),
                'location': filter_location(post),
                'tags': filter_tags(post),
                })


def filter_title(job):
    """Filter out job title and link to listing."""
    job_title = job.find('a', attrs={'class': 'job-link'}).text
    link = job.find('a', href=True).attrs['href']
    job_link = 'https://stackoverflow.com{}'.format(link)
    return(job_link, job_title)


def filter_time(job):
    """Filter out job title and link to listing."""
    time = job.find('p', attrs={'class': '-posted-date'})
    post_time = time.text.strip()
    return post_time


def filter_company(job):
    """Filter out company name."""
    company_container = job.find('div', attrs={'class': '-name'})
    company_name = company_container.get_text().strip()
    return company_name


def filter_location(job):
    """Filter out job location."""
    location_container = job.find('div', attrs={'class': '-location'})
    company_location = location_container.text.strip().lstrip('-').strip()
    return company_location


def filter_tags(job):
    """Filter out tags attached to post."""
    tag_list = ''
    tag_container = job.find('div', attrs={'class': '-tags'})
    job_tags = tag_container.findAll('a', attrs={'class': 'post-tag'})
    for tag in job_tags:
        tag_list += '{}, '.format(tag.text)
    return tag_list


if __name__ == '__main__':
    url = 'https://stackoverflow.com/jobs?sort=i&q=python&l=United+States&d=100&u=Miles'
    scrape_page(url)
    # for i in range(2, 11):
    #     page = 'https://stackoverflow.com/jobs?q=python&l=United+States&d=100&u=Miles&sort=i&pg={}'.format(i)
    #     scrape_page(page)
