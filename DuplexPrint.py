#!/usr/bin/python3
import argparse
from PyPDF2 import PdfReader
import os
import subprocess
#############################################################
parser = argparse.ArgumentParser(description='Print PDF pages in Duplex mode using a single function printer')
parser.add_argument('filename')# positional argument
args = parser.parse_args()
#############################################################
def evenRangeRev(end,start=1):
	end= end if end % 2 == 0 else end-1
	# iterating each number in list
	rng=range(end,start,-2)
	return(rng)
#############################################################
def getPDFPages(filename):
	reader = PdfReader(filename)
	numPages = len(reader.pages)
	return(numPages)
#############################################################
def printFile(filename):
	pageCount= getPDFPages(filename)
	print("Total number of pages = "+str(pageCount))
	##CMD="lpr -o sides=two-sided-short-edge "+filename
	##print(CMD)
	############################################
	oddPages=range(1, pageCount, 2) 
	for i in oddPages:
		print("Printing page "+str(i)+"/"+str(pageCount))
		CMD="lpr -o page-ranges="+str(i)+" "+filename
		#os.system(CMD)
		#p = subprocess.Popen(CMD.split())
		#p.wait()
		#print(CMD)
	############################################
	inp = input('Please wait till the printer stops\n and then place the pages in tray.\n Now enter to continue ...')
	############################################
	evenPages=evenRangeRev(pageCount) 
	for i in evenPages:
		print("Printing page "+str(i)+"/"+str(pageCount))
		CMD="lpr -o page-ranges="+str(i)+" "+filename
		p = subprocess.Popen(CMD.split())
		p.wait()
		#print(CMD)
#############################################################
printFile(args.filename)