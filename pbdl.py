#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Packtpub Downloader
"""


import sys
import os
import argparse
import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


__author__ = "Anthony Da Mota"
__credits__ = ["Anthony Da Mota"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Anhony Da Mota"
__email__ = "anthony@damota.me"
__status__ = "Development"


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Packtpub username", required=True)
    parser.add_argument("-p", "--password", help="Packtpub password", required=True)
    args = parser.parse_args()
    return args


def clearAndWrite():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print "[PacktPub Downloader v0.1]\n"


def get_user_agent():
    return UserAgent().random


def valid_filename(text, title=False):
    output = ""
    if title:
        output = text.replace(" [eBook]", "")
        output = re.sub('\W', '_', output)
    else:
        output = re.sub('\W', '_', text)
    return output


def main(argv):
    args = arguments()
    login_username = args.username
    login_password = args.password
    base_url = "https://www.packtpub.com"
    ebooks_url = "{}/account/my-ebooks".format(base_url)
    req = requests.Session()

    try:
        headers = { 'User-Agent' : get_user_agent(), "Referer": base_url }
        login_data = {
            "email": args.username,
            "password": args.password,
            "op": "Login",
            "form_id": "packt_user_login_form"
        }
        the_login = req.post(base_url, data=login_data, headers=headers)

        the_books = req.get(ebooks_url, headers=headers)
        books_soup = BeautifulSoup(the_books.text, 'html.parser')

        product_account_list = books_soup.find(attrs={"id": "product-account-list"})

        for product in product_account_list.find_all("div", {"class": "product-line"}):
            if 'title' in product.attrs:
                title = product.attrs['title']
                print valid_filename(title, True)
                # for link in product.find('div', {'class': 'product-buttons-line'}).select('div.download-container')[1].find_all('a'):
                #     if link.attrs['href'] != "#":
                #         print "{}{}".format(base_url, link.attrs['href'])

    except KeyboardInterrupt:
        print "\nExiting...\n"
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
