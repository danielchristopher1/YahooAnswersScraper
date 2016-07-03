# YahooAnswersScraper
Python script that uses beautiful soup to scrape a yahoo answers page and return the answers.

# Dependencies
- Install Python 2.7 or 3.5
- pip install beautifulsoup4
- pip install requests

# Example

```python
from scraper import YahooScraper    

scraper = YahooScraper()
answers = scraper.get_answers('https://answers.yahoo.com/question/index?qid=20160625002028AACkxqK')

print answers
```
