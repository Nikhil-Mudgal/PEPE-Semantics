import concurrent.futures
from pathlib import Path
from typing import Tuple

import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
from tqdm import tqdm


## Slower method
class GetImageData:  # Slower method
    def __init__(
        self,
        dataset: pd.DataFrame,
        colname="Meme Page URL",
        meme_name="Base Meme Name",
        path="Image_Store",
    ):
        self.dataset = dataset
        self.colname = colname
        self.meme_name = meme_name
        self.path = path

    def page_scrapper(self, link: str) -> bs4.BeautifulSoup:
        """Gets the data from page

        Args:
            link (str): page link to check the file from, stored in df for our case

        Returns:
            bs4.BeautifulSoup: contains information contained in page url
        """
        response = requests.get(link)
        data = response.text
        soup = BeautifulSoup(data, "lxml")
        return soup

    def comment_scapper(self, soup: bs4.BeautifulSoup) -> str:
        """Scrapes the required url from comments

        Args:
            soup (bs4.BeautifulSoup): Instance contaning the info of page url

        Returns:
            str: url for the affiliated picture in the page
        """
        query = ["dataobject", {"type": "image"}]
        store: bs4.element.Comment = soup.find(
            string=lambda text: isinstance(text, Comment)
        )
        commentsoup = BeautifulSoup(store, "lxml")
        commentsoup = commentsoup.find(query)
        return commentsoup.attribute["value"]

    def save_path(self) -> Path:

        store_path = Path(self.path) if Path(self.path).exists() else Path(self.path)
        store_path.mkdir(parents=True, exist_ok=True)
        return store_path

    def get_image_urls(self, url_list) -> list:
        urls = []
        for idx in tqdm(range(len(url_list))):
            soup = self.page_scrapper(url_list[idx])
            url = self.comment_scapper(soup=soup)
            urls.append(url)
        return urls

    def image_metadata(self) -> dict:
        metadata = {}
        for idx in tqdm(range(len(self.dataset[self.colname]))):
            meme_name = self.dataset[self.meme_name][idx]
            soup = self.page_scrapper(self.dataset[self.colname[idx]])
            url = self.comment_scapper(soup=soup)
            metadata[meme_name] = url
        return metadata

    def save_images(self) -> None:
        """Saves the images in default `Image_Store` Folder"""
        path = self.save_path()  # creating the save directory
        urls = self.get_image_urls()
        for idx in tqdm(range(len(urls))):
            r = requests.get(urls[idx])
            filename = path / f"{urls[idx].split('/')[-1]}"
            with open(filename, "wb") as f:
                f.write(r.content)
