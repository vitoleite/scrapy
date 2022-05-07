from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bcb_web_scrapy",
    version="0.0.4",
    author="vitor_leite",
    author_email="vitorleite5@outlook.com",
    description="Project focused to learn web scrape",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitoleite/scrapy",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    license='MIT'
)