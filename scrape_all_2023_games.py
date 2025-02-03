import bs4
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
import time
import random
from IPython.display import clear_output, display

## Constants

# Rate limit of requests that can be made to baseball reference to avoid their spam jail
REQUESTS_PER_MINUTE = 20

teams = [
    "ARN",
    "ATL",
    "BAL",
    "BOS",
    "CHA",
    "CHN",
    "CIN",
    "CLE",
    "COL",
    "DET",
    "HOU",
    "KCA",
    "LAA",
    "LAN",
    "MIA",
    "MIL",
    "MIN",
    "NYA",
    "NYN",
    "OAK",
    "PHI",
    "PIT",
    "SDN",
    "SFN",
    "SEA",
    "STL",
    "TBA",
    "TEX",
    "TOR",
    "WAS",
]
, gameID, ds

time.sleep(60/REQUESTS_PER_MINUTE)

def scrape_wpa(url) -> 'WPA DataFrame':
    # web scraping stuff
    req = requests.get(url)
    resp = req.status_code
    d = soup(req.text, 'html.parser')
    # if page exists
    if resp == 200:
        # only scrape the WPA table data from the html response
        block = [i for i in d.find_all(string=lambda text: isinstance(text, bs4.Comment)) if 'id="div_play_by_play"' in i][0]
        b = soup(str(block), 'html.parser')
        table = b.find_all('table')
        df = pd.read_html(str(table))[0]
        df.to_csv(path)
        wpa_data = ingestDF(df, gameID, path, ds)
        # Return WPA data in form of a dataframe
        return wpa_data
    else:
        return None


