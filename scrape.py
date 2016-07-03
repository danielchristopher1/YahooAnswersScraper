from bs4 import BeautifulSoup
import requests

class YahooScraper:
    def get_answers(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        results = soup.find_all('span', class_='ya-q-full-text')
        return [answer.text for answer in results]
