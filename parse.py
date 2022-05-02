from dataclasses import dataclass
from email import header
import requests
import lxml
from bs4 import BeautifulSoup
import time
import csv

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'

}

def calories(url):
    
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')

    data = []

    calor_item = soup.find('div', class_ = "elementor-accordion").find_all('tr')

    for cal in calor_item:
        calor_item_data = cal.find_all('td')

        try: 
            pavadinimas = calor_item_data[0].find('p').text.strip()
        except:
            pavadinimas = '-'
        
        try:
            kalorijos = calor_item_data[1].find('p').text
        except:
            kalorijos = '-'
        
        try:
            angliavandeniai = calor_item_data[2].find('p').text
        except:
            angliavandeniai = '-'
        try:
            baltymai = calor_item_data[3].find('p').text 
        except:
            baltymai = '-' 
        
        try:
            riebalai = calor_item_data[4].find('p').text
        except:
            riebalai = '-'

        data.append([pavadinimas, kalorijos, angliavandeniai, baltymai ,riebalai])
        

        header = ['pavadinimas', 'kalorijos', 'angliavandeniai', 'baltymai' ,'riebalai']

        with open ('kalorijos.csv', 'w' , encoding="utf-8") as f:
             writer = csv.writer(f)
             writer.writerow(header)
             writer.writerows(data)
             print(data)


def main():

    calories (url = 'https://sportuojantys.lt/kaloriju-skaiciuokle/')

if __name__ == '__main__':
    main()