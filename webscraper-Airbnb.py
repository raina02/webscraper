import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.co.in/?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&search_mode=flex_destinations_search&flexible_trip_lengths%5B%5D=one_week&location_search=MIN_MAP_BOUNDS&monthly_start_date=2024-05-01&monthly_length=3&monthly_end_date=2024-08-01&category_tag=Tag%3A677&price_filter_input_type=0&channel=EXPLORE&guest_favorite=true&search_type=filter_change'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Location':[''], 'Price':[''], 'Rating':['']})

if soup.status_code == 200:

    postings = soup.find_all('div', class_='lxq01kf')
    for post in postings:
        try:
            price = post.find('span', class_='_1y74zjx').text
            rating = post.find('span', class_='ru0q88m').text
            location = post.find('div', class_='t1jojoys').text

            df = df.append({'Location':location, 'Price':price, 'Rating':rating}, ignore_index = True)
            df.to_csv('/home/satyam/workspace/webscraper/ScrapedData/airbnb_scraped_data.csv')
        except:
            break

