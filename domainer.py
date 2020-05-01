#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Domainer simple domain checker (https://domainr.com/)
# By Locu

import os
import sys
import argparse
import urllib.request
import bs4
import fileinput
import colorama
from colorama import Fore, Style
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--domain', help='Input domain (google.com)', action='store')
parser.add_argument('-l', '--list', help='Input domains.txt', action='store')
parser.add_argument('-x', '--ex', help='load excluded domains list', action='store')


if len(sys.argv)<2:
	print('eg: python %s -l domainlist' % sys.argv[0])
	args = parser.parse_args(['-h'])
else:
	args = parser.parse_args()


def check_domain(domain):
	try:
		url = ("https://domainr.com/?q=" + domain)
		s = urllib.request.urlopen(url)
		mybytes = s.read()
		out = mybytes.decode("utf8")
		s.close()
		soup = BeautifulSoup(out, "html.parser")

		res = str(soup.find("div", { "class" : "domain-status" }))
		if "Available" not in res: 
			print(domain + Fore.RED  +  ' --> Taken')
		elif "Taken" not in res:
		  print(domain + Fore.BLUE  + ' --> Available')
		else:
		  print ('Something goes wrong *-*')
	except:
		pass


if args.domain:
	check_domain(args.domain)
	print(Style.RESET_ALL)

if args.list:
		if args.ex:
			with open(args.ex) as file:
				ex = [i.strip() for i in file]
		else:
			with open('exclusions.dat') as file:
				ex = [i.strip() for i in file]

		domains = filter(None, open(args.list, 'r').read().splitlines())
		for d in domains:
			if d not in ex:
				check_domain(d)
				print(Style.RESET_ALL)

			




	  
