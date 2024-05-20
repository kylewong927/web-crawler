import requests
from bs4 import BeautifulSoup

def start_crawler(url):
    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        if soup.title:
            page_title = soup.title.text
            print(f'Title of the webpage is: {page_title}')

        links = [a['href'] for a in soup.find_all('a', href=True)]
        print(f'Total number of links on the page: {len(links)}')
        if len(links) > 0 :
            for link in links:
                print(f'{link}')

        for paragraph in soup.find_all('p'):
            print(f'{paragraph.text}')