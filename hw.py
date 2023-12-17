import requests
from bs4 import BeautifulSoup

url = "https://tengrinews.kz/news/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a', href="https://www.liveinternet.ru/click")
    for i, link in enumerate(links, start=1):
        print(f"{i}. {link['href']}")

else:
    print(f"Ошибка при получении страницы: {response.status_code}")