from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())
 
#para achar algo especific use , EXEMPLO:
'''
temperatura = soup.find('span', class_ = 'block _margin-b-5 - gray')
print(temperatura.string)
print(soup.find('admin'))
'''