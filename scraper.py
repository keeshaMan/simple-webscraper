import requests
import certifi
from bs4 import BeautifulSoup
import csv

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
    
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(['Titile', 'Text', 'Link'])

        writer.writerow([title,text,link])
        print("data saved to scraped_data.csv")
        
if __name__ == '__main__':
    scrape()