#import packages
import csv
import re
import pandas as pd

#declarations
lines = []
j = 0

filename = input("Enter name of csv to split (include the extension in the filename): ")
splitsize = input("Enter the number of rows expected in every split file: ")
splitsize = int(splitsize)
with open(filename) as fileobject:
	for line in fileobject:
		lines.append(line)

partindices = [i for i in range(1,len(lines)-1,splitsize)]
for partindex in partindices:
	j+=1
	print("Working on file:",filename[:-4]+'_split_'+str(j)+'.csv')
	line = lines[0]
	matches = re.finditer(',',line)
	ind1 = [match.start() for match in matches]
	ind = [0]
	for element in ind1:
		ind.append(element)
	firstpart = [line[0:ind1[0]].split()]
	parts = [line[ind[i]:ind[i+1]][1:].strip() for i in range(len(ind)-1)]
	parts[0] = line[0]+parts[0]
	with open(filename[:-4]+'_split_'+str(j)+'.csv', mode='a',encoding='utf-8') as csvobject:
		csv_writer = csv.writer(csvobject, delimiter=',', quotechar='"')
		csv_writer.writerow(parts)

	for line in lines[partindex:partindex+splitsize-1]:
		matches = re.finditer(',',line)
		ind1 = [match.start() for match in matches]
		ind = [0]
		for element in ind1:
			ind.append(element)
		firstpart = [line[0:ind1[0]].split()]
		parts = [line[ind[i]:ind[i+1]][1:].strip() for i in range(len(ind)-1)]
		parts[0] = line[0]+parts[0]
		with open(filename[:-4]+'_split_'+str(j)+'.csv', mode='a',encoding='utf-8') as csvobject:
		    csv_writer = csv.writer(csvobject, delimiter=',', quotechar='"')
		    csv_writer.writerow(parts)
print("Cleaning newly generated csvs...")
for i in range(1,j+1):
    df = pd.read_csv(filename[:-4]+'_split_'+str(i)+'.csv')
    df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    df.to_csv(filename[:-4]+'_split_'+str(i)+'.csv', index = False)
