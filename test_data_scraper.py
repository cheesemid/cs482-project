import pytest
import data_scraper
import os
from bs4 import BeautifulSoup


def test_image_dl():
    data_scraper.dl_imgs("test", ["https://images.thdstatic.com/productImages/89534bf7-6fcb-4c51-a9b1-be7a69c4da69/svn/spot-resist-brushed-nickel-moen-towel-bars-y2622bn-64_300.jpg"])
    assert "test_0.png" in os.listdir("data")
    os.remove("data/test_0.png")

def test_link_getting():
    img_links = data_scraper.get_category("mirror")
    assert len(img_links) == 100

def test_html_get():
    soup = data_scraper.get_html("https://www.homedepot.com/b/Bath-Toilets-One-Piece-Toilets/N-5yc1vZcb8v")
    assert isinstance(soup, BeautifulSoup)
