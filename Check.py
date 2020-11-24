#Script to utilize the "achecker.py" program for the site list

import csv
from aChecker import *

with open('mycsvfile.csv','r')as csv_file:
	csv_reader=csv.DictReader(csv_file)

	with open('Last.csv','w')as last_file:
		fieldnames=['Sites','Tested','Known','Likely','Potential']
		csv_writer=csv.DictWriter(last_file,fieldnames=fieldnames)
		csv_writer.writeheader()

		for line in csv_reader:
			if line['Tested']!='Y':
				csv_writer.writerow(check(line['Sites']))
			else:
				csv_writer.writerow(line)
