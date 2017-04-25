#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Packtpub Free Ebook Getter
"""


import sys
import os
import argparse
import requests
import re
from bs4 import BeautifulSoup


__author__ = "Anthony Da Mota"
__credits__ = ["Anthony Da Mota"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Anhony Da Mota"
__email__ = "anthony@damota.me"
__status__ = "Development"


def arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("-u", "--username", type=str, help="Packtpub username", required=True)
  parser.add_argument("-p", "--password", type=str, help="Packtpub password", required=True)
  parser.add_argument("-s", "--sms", action="store_true", help="Send as SMS")
  args = parser.parse_args()
  return args


def clear_and_write():
  if os.name == "nt":
      os.system("cls")
  else:
      os.system("clear")
  print "[PacktPub Free Ebook Getter v{}]\n".format(__version__)


def get_user_agent():
  return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"


def claim_free_ebook(login_username, login_password, base_url, free_ebook_url, sms):
  req = requests.Session()

  try:
    if not sms:
      clear_and_write()
      print "Logging in..."

    headers = {'User-Agent' : get_user_agent(), "Referer": base_url}
    login_data = {
        "email": login_username,
        "password": login_password,
        "op": "Login",
        "form_id": "packt_user_login_form"
    }
    the_login = req.post(base_url, data=login_data, headers=headers)

    if the_login.status_code == 200:
      if not sms:
        print "Login success!\n"

      free_ebook_url_get = req.get(free_ebook_url, headers=headers)
      free_ebook_soup = BeautifulSoup(free_ebook_url_get.text, 'html.parser')

      free_ebook_name = free_ebook_soup.find("div", attrs={"class": "dotd-title"}).find('h2').text
      free_ebook_name = " ".join(free_ebook_name.split())
      if not sms:
        print "Free ebook of the day: \"{}\"".format(free_ebook_name.encode('utf-8'))

      claim_ebook_url = free_ebook_soup.find("a", attrs={"class": "twelve-days-claim"}).get('href')

      full_claim_ebook_url = "{}{}".format(base_url, claim_ebook_url)

      claim_ebook = req.get(full_claim_ebook_url, headers=headers)

      if claim_ebook.status_code == 200:
        if not sms:
          print "Ebook \"{}\" has been successfully downloaded to your PacktPub account 👌".format(free_ebook_name.encode('utf-8'))
        else:
          print "Ebook \"{}\" has been successfully downloaded to your PacktPub account.".format(free_ebook_name.encode('utf-8'))
    else:
      if not sms:
        print "\nLogin failed. Please check credentials.\n"
      else:
        print "PacktPub: Login failed. Please check credentials."

  except KeyboardInterrupt:
    if not sms:
      print "\nExiting...\n"
    sys.exit()


def main(argv):
  args = arguments()
  login_username = args.username
  login_password = args.password
  sms = False
  if args.sms:
    sms = True
  base_url = "https://www.packtpub.com"
  free_ebook_url = "{}/packt/offers/free-learning".format(base_url)

  claim_free_ebook(login_username, login_password, base_url, free_ebook_url, sms)


if __name__ == "__main__":
  main(sys.argv[1:])
