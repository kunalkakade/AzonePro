import requests
from bs4 import BeautifulSoup




URL_LIST = ['https://github.com/MrAlex6204/Books'] #'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'


def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

for i in URL_LIST:
    get_data(i)


