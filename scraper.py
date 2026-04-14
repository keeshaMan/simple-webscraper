import requests
import certifi
from bs4 import BeautifulSoup

def scrape():
    url = 'http://www.example.com'
    response = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')
    
    print(title)
    print(text)
    print(link)

if __name__ == '__main__':
    scrape()