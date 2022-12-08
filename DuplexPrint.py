#!/usr/bin/python3
import argparse
from PyPDF2 import PdfReader
import os
import subprocess
import time
#############################################################
parser = argparse.ArgumentParser(description='Print PDF pages in Duplex mode using a single function printer')
parser.add_argument('filename')# positional argument
parser.add_argument('-o', '--odd', help='Enable if ODD pages require printing',action='store_true', default=False)
parser.add_argument('-e', '--even', help='Enable if EVEN pages require printing',action='store_true',default=False)
parser.add_argument('-f', '--from', help='Start printing from page number',default=1)
parser.add_argument('-t', '--till', help='Continue printing till page number',default=None)
args = parser.parse_args()
#############################################################
def oddRange(end,start=1):
	end= start+1 if start % 2 == 0 else start
	# iterating each number in list
	rng=range(start,end,2)
	return(rng)
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
def waitPrint():
	isPrintPending=True
	while (isPrintPending):
		CMD="lpstat"
		p = subprocess.run(CMD.split(), capture_output=True, text=True)
		isPrintPending=True if(len(p.stdout)>0) else False
		if(isPrintPending):
			print("There are still" len(p.stdout.split("\n")) "pending jobs as follows:\n")
			print(p.stdout)
			print("Don't worry. I'll wait for 10s and retry")
			time.sleep(10)
#############################################################
def printFile(filename):
	pageCount= getPDFPages(filename)
	print("Total number of pages = "+str(pageCount))
	##CMD="lpr -o sides=two-sided-short-edge "+filename
	##print(CMD)
	############################################
	evenPages=oddPages(pageCount)
	for i in oddPages:
		print("Printing page "+str(i)+"/"+str(pageCount))
		CMD="lpr -o page-ranges="+str(i)+" "+filename
		#os.system(CMD)
		p = subprocess.Popen(CMD.split())
		p.wait()
		#print(CMD)
	############################################
	waitPrint()
	inp = input('ODD page printing complete.\n Now take the printed pages from output tray and place in feeder tray and \nPRESS any key to continue ...')
	############################################
	evenPages=evenRangeRev(pageCount) 
	for i in evenPages:
		print("Printing page "+str(i)+"/"+str(pageCount))
		CMD="lpr -o page-ranges="+str(i)+" "+filename
		p = subprocess.Popen(CMD.split())
		p.wait()
		#print(CMD)
	waitPrint()
	print("Print task completed !!")
#############################################################
printFile(args.filename)