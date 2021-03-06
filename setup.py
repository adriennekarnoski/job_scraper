from setuptools import setup

setup(
    name="job_scraper",
    version='0.0',
    description="Job Scraper",
    author="Adrienne Karnoski",
    author_email="adrienne.j.karnoski@gmail.com",
    py_modules=[
        'scrape',
        'job_data',
        ],
    install_requires=[
        'beautifulsoup4.',
        'pandas',
        'numpy',
        'datetime',
        'matplotlib',
        'collections'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov']},
    package_dir={"": "src"}
)