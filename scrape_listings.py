"""
Goal: JSONify the important contents of edgar.
Strategy:
    1. The url of all the pages

"""
import json
import requests
import sys
from bs4 import BeautifulSoup as Bs

BASE_URL = 'http://data-interview.enigmalabs.org/companies/'


def _main():
    pages = get_pages(BASE_URL)
    links = get_links(pages)
    tables = get_tables(links)


def get_pages(url):
    """
    Retrieves the different pages on edger

    :param url: URL where all the pages are to be found
    :return: list of all the pages of the website
    """
    pages = [BASE_URL + '?page={}'.format(i) for i in range(2,11)] # Pages 2-10
    pages.append(BASE_URL) # The first page

    assert len(pages) == 10

    return pages


def get_links(urls):
    """
    Gets all of the links based on a list of urls

    :return: Lists of links to individual movies.

    """
    links = []
    for url in urls:
        r = requests.get(url)
        soup = Bs(r.text)

        # Only one table on the website
        table = soup.find_next('tbody')
        links = table.find_all('a')
        links.append(links)
    return links


def get_tables():
    """

    Returns
    -------

    """
    x_path = r'/html/body/div[2]/div/table'

if __name__ == '__main__':
    sys.exit(_main())

