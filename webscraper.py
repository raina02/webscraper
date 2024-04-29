import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.makemytrip.com/hotels/hotel-listing/?checkin=05012024&city=CTGOI&checkout=05022024&roomStayQualifier=2e0e&locusId=CTGOI&country=IN&locusType=city&searchText=Goa&regionNearByExp=3&rsc=1e2e0e'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
response = requests.get(url, headers=headers)
df = pd.DataFrame({'Name':[''], 'Location':[''], 'Price':[''], 'Rating':['']})
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('div', class_='listingRowOuter')
        
    for listing in listings:
        name = listing.find('span', class_='wordBreak').text
        location = listing.find('span', class_='blueText').text
        price = listing.find('p', class_='priceText').text
        rating = listing.find('span', class_='rating').text

        df = df.append({'Name': name, 'Location':location, 'Price':price, 'Rating':rating}, ignore_index = True)
        df.to_csv('/home/satyam/workspace/webscraper/ScrapedData/makemytrip_scraped_data.csv')

    else:
        print("Failed to retrieve page")
