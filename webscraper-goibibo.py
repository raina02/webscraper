import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.goibibo.com/hotels/find-hotels-in-Hyderabad,%20Telangana,%20India/2162254155836171767/2162254155836171767/%7B%22ci%22:%2220240504%22,%22co%22:%2220240505%22,%22r%22:%221-2-0%22%7D/?{%22filter%22:{}}&sec=dom&cc=IN&locusId=CTHYDERA&locusType=city&cityCode=CTHYDERA'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Name':[''], 'Location':[''], 'Price':[''], 'Rating':['']})

if soup.status_code == 200:

    postings = soup.find_all('div', class_='bCcJmq')
    for post in postings:
        try:
            name = post.find('h4', class_='iBfmPW').text
            location = post.find('div', class_='hpnrYJ').text
            price = post.find('p', class_='bMcDRf').text
            rating = post.find('span', class_='ijVBFh').text

            df = df.append({'Name': name, 'Location':location, 'Price':price, 'Rating':rating}, ignore_index = True)
            df.to_csv('/home/satyam/workspace/webscraper/ScrapedData/goibibo_scraped_data.csv')
        except:
            break

