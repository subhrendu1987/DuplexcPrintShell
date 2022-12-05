#!/usr/bin/python3
import argparse
from PyPDF2 import PdfReader
import os
#############################################################
parser = argparse.ArgumentParser(description='Print PDF pages in Duplex mode using a single function printer')
parser.add_argument('filename')           # positional argument

args = parser.parse_args()
#############################################################
def getPDFPages(filename):
	reader = PdfReader(filename)
	numPages = len(reader.pages)
	return(numPages)
#############################################################
def printFile(filename):
	pageCount= getPDFPages(filename)
	print(pageCount)
	CMD="lpr -o sides=two-sided-short-edge "+filename
	print(CMD)
	print("Printing ODD pages")
	CMD="lpr -o page-set=odd "+filename
	#os.system(CMD)
	print(CMD)
	inp = input('Please wait till the printer stops and then enter to continue ...')
	print("Printing EVEN pages")
	CMD="lpr -o page-set=even -o outputorder=reverse "+filename
	#os.system(CMD)
	print(CMD)
#############################################################
printFile(args.filename)