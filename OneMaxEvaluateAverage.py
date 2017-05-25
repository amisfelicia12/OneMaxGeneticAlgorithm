#script to compute the average for multiple loops
from openpyxl import load_workbook
import csv
import numpy as np
import pandas as pd
import xlsxwriter

gn0 = np.empty(shape=[32,31])
gn0.fill(20)


for i in range(0,30,1):
	nameOfFile = 'file'+str(i)+'.csv'
	ifile = open(nameOfFile,'rb')
	reader = csv.reader(ifile)
	j = 0
	for row in reader:
		listof = row[0].split( )
		generation = int(listof[0])
		fitness = int(listof[1])
		if generation == j:
			gn0[j,i] = fitness
			j = j+1

avgFitness = []
for k in range(0, 30, 1):
	avgFitness.append(np.average(gn0[k]))

####################################################################
gn1 = np.empty(shape=[32,31])
gn1.fill(20)
l=0
for m in range(0,30,1):
	nameOfFile = 'AdvFile'+str(m)+'.csv'
	ifile = open(nameOfFile,'rb')
	reader = csv.reader(ifile)
	l = 0
	for row in reader:
		listof = row[0].split( )
		generation = int(listof[0])
		fitness = int(listof[1])
		if generation == l:
			gn1[l,m] = fitness
			l = l+1

avgFitnessAdvanced = []

for k in range(0, 32, 1):
	avgFitnessAdvanced.append(np.average(gn1[k]))
########################################################
tn0 = np.zeros(shape=[32,1])
for i in range(0,30,1):
	nameOfFile = 'time'+str(i)+'.csv'
	ifile = open(nameOfFile,'rb')
	reader = csv.reader(ifile)
	for row in reader:
		listof = row[0].split( )
		tiempo = float(listof[0])
		tn0[i,0] = tiempo

avgTiempo = []
for k in range(0, 31, 1):
	avgTiempo.append(np.average(tn0[k]))

####################################################################
tn1 = np.zeros(shape=[32,1])
for m in range(0,30,1):
	nameOfFile = 'AdvTime'+str(m)+'.csv'
	ifile = open(nameOfFile,'rb')
	reader = csv.reader(ifile)
	for row in reader:
		listof = row[0].split( )
		tiempo = float(listof[0])
		tn1[m,0] = tiempo

avgTiempoAdvanced = []
for k in range(0, 32, 1):
	avgTiempoAdvanced.append(np.average(tn1[k]))

####################################################################
th1 = np.zeros(shape=[32,1])
for m in range(0,30,1):
	nameOfFile = 'ThreadTime'+str(m)+'.csv'
	ifile = open(nameOfFile,'rb')
	reader = csv.reader(ifile)
	for row in reader:
		listof = row[0].split( )
		tiempo = float(listof[0])
		tn1[m,0] = tiempo

avgThreadTime = []
for k in range(0, 32, 1):
	avgThreadTime.append(np.average(th1[k]))

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Average Fitness for 30 loops in Simple Mutation': avgFitness})
df1 = pd.DataFrame({'Average Fitness for 30 loops in Advanced Mutation': avgFitnessAdvanced})
dt = pd.DataFrame({'Time Taken in Simple Mutation': avgTiempo})
dt1 = pd.DataFrame({'Time Taken in Advanced Mutation': avgTiempoAdvanced})
dh1 = pd.DataFrame({'Time Taken by Thread implementation': avgThreadTime})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('OneMaxSimpleMutation.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')
df1.to_excel(writer,sheet_name='Sheet2')
dt.to_excel(writer, sheet_name='Sheet3')
dt1.to_excel(writer,sheet_name='Sheet4')
dh1.to_excel(writer,sheet_name='Sheet5')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
