# Job Scraper and Job Analysis

This repository contains two files, **scrape.py** and **job_data.py**, along with a CSV file and tests.

## Introduction

### scrape.py

This file, when run, will crawl the first ten pages of [StackOverflow Jobs](https://stackoverflow.com/jobs?sort=i&q=python&l=United+States&d=100&u=Miles)
and store the information collected in **jobs.csv**. 

The categories collected are:
* URL
* Title
* Post date
* Company
* Location
* Post tags

### job_data.py


## Setup

Clone the repository and move into the **src** directory:
```
$ git clone https://github.com/adriennekarnoski/job_scraper`
$ cd python
```

Start your virtual environment:
```
$ python3 -m venv ENV
$ source bin/ENV/activate
```

Install package

`$ (ENV) pip install -e .`

**testing**
```
$ (ENV) pip install -e .[test]
```
***
