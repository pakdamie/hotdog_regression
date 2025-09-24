import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import requests

#Hotdog prices
def retrieve_hotdog_prices():
    """
    Retrieve hotdog price data from Datawrapper.

    Returns:
        pd.DataFrame: A DataFrame containing team names and hotdog prices.
    """

    url = "https://datawrapper.dwcdn.net/MjCwJ/2/dataset.csv"  
    
    response = requests.get(url)
    response.raise_for_status() 

    df = pd.read_csv(url,sep="\t")
     #Tab delimited not comma delimited
    return df


def retrieve_bb_stadium_wiki():
    """
    Pull out the necessary baseball stadiums data from Wikipedia.
    """
    url = "https://en.wikipedia.org/wiki/List_of_current_Major_League_Baseball_stadiums"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    
    table_df = pd.read_html(str(tables[0]))[0]
    return table_df
