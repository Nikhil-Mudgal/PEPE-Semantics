from typing import Tuple
import bs4
import requests
import pandas as pd 
import concurrent.futures
from tqdm import tqdm
from bs4 import Comment
from pathlib import Path 
from bs4 import BeautifulSoup


# Getting the dataset ready

FILE_LOC = "memegenerator.csv" 
REMOVE_STR = "http://webarchive.loc.gov/all/0/"

def get_page_url(file=FILE_LOC,remove_str=REMOVE_STR) -> list:
    """Prepares the dataset 

    Args:
        file (str, optional): csv file containing the dataset. Defaults to FILE_LOC.
        remove_str (str, optional): remove string from explored data. Defaults to REMOVE_STR.

    Returns:
        pd.DataFrame: dataset to work with
    """
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    df["Meme Page URL"] = [items.replace(remove_str,'') if items.startswith(remove_str) else items for items in df["Meme Page URL"]] 
    drop_cols = ["Meme ID", "Archived URL", "MD5 Hash","File Size (In Bytes)"]
    df.drop(drop_cols,axis=1,inplace=True)
   
    return df["Meme Page URL"].to_list()

url_list = get_page_url()

class PrepareImageURL(): # much more faster than scraping from Website
    """
    Convert the "MEME PAGE URL" columns entities to the format
    
    """
    URL_HEAD = "https://memegenerator.net/img/instances/"
    IMAGE_URL_LIST = []
    def __init__(self,url_list:list):
        self.url_list = url_list
        
    def prepare_urls(self):
        for url in self.url_list:
            ids = url.split("/")[-1]
            new_url = PrepareImageURL.URL_HEAD + ids + ".jpg"
            PrepareImageURL.IMAGE_URL_LIST.append(new_url)
        return PrepareImageURL.IMAGE_URL_LIST
    
url_list = PrepareImageURL(url_list).prepare_urls()

def save_paths() -> tuple[Path,Path]:
    """Creates save paths to store the data

    Returns:
        _type_: _description_
    """
    path1 = Path("image_store") if Path("image_store").exists() else Path("image_store")
    path2 = Path("url_stores") if Path("url_stores").exists() else Path("url_stores")
    path1.mkdir(parents=True,exist_ok=True)
    path2.mkdir(parents=True,exist_ok=True)

    return path1,path2 

image_store,url_stores = save_paths()

pd.DataFrame(url_list).to_csv(url_stores / "image_urls.csv") # updates per run of the program


## Faster method supplied with Parallel Processing 
def save_image(url,path=image_store):
    r = requests.get(url)
    filename = path / url.split('/')[-1]
    with open(filename,"wb") as f:
        f.write(r.content)


# Saves image data onto the disk for faster use..

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(save_image, url_list)
