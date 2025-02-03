import bs4
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
import time
import random
from IPython.display import clear_output, display

def getSeasonScheduleHTML(year) -> 'soup':
    url = f"https://www.baseball-reference.com/leagues/majors/{year}-schedule.shtml"
    req = requests.get(url)
    resp = req.status_code

    if resp == 200: return(soup(req.text, 'html.parser'))
    
    # if the page does not exist, return None
    return None

        

import statsapi
def main(): 
    # print(getSeasonScheduleHTML(2023))
    games = statsapi.schedule(start_date='2023-01-01', end_date='2023-12-31')

if __name__ == '__main__':
    main()
