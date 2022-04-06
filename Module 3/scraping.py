from requests import get
from contextlib import closing
from bs4 import BeautifulSoup


def get_a_page(url):
    header = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
    with closing(get(url, headers=header)) as resp:
        return resp


raw_html = get_a_page("https://desmoines.craigslist.org/d/recreational-vehicles/search/rva")

html = BeautifulSoup(raw_html.text, 'html.parser')
postings = html.find_all('li', class_='result-row')
print(type(postings))
print(len(postings))
post_1_price = postings[0].a.text
post_1_price = post_1_price.strip()
print(post_1_price)
post_1_time = postings[0].find('time', class_='result-date')
post_1_datetime = post_1_time['datetime']
print(post_1_datetime)
post_1_title = postings[0].find('a', class_='result-title hdrlnk')
post_1_link = post_1_title['href']
print(post_1_link, post_1_title.text)
post_1_location = postings[0].find(class_= 'result-hood')
print(post_1_location.text)
