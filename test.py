import csv
import matplotlib.pyplot as mpl
import os
from numpy import *
from matplotlib.pyplot import cm
os.chdir('C:\\Users\\Administrator\\Desktop\\COMP6730')
with open("daily-max-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    data_max = [ [row[2],row[3],row[4],row[5]] for row in reader if row[3]>= '06' and row[3]<='08']
    
# print(data_max)
print(len(data_max))
with open("daily-min-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    data_min = [ [row[2],row[3],row[4],row[5]] for row in reader if row[3]>= '06' and row[3]<='08']
    
print('-----')

data_avg = []
# print(data_min)
print(len(data_min))
for i in range(len(data_max)-1):
    if data_max[i][0:3] == data_min[i][0:3]:
        if data_max[i][3] != '' and data_min[i][3] != '':
            data_avg.append(data_max[i][0:3]+[round((float(data_max[i][3])+float(data_min[i][3]))/2,2)])
data_com = []
for i in range(2008,2022):
    total_date = 0
    sum = 0
    for x in data_avg:
        if i == int(x[0]):
            total_date+=1
            sum+=x[3]
    if total_date!=0:
        data_com.append([i]+[round(sum/total_date,2)])
print(data_com)
x = [i[0] for i in data_com]
y = [i[1] for i in data_com]
mpl.bar(x,y,color = cm.rainbow([ i/len(data_com) for i in range(len(data_com))]))
mpl.xlabel('years')
mpl.ylabel('ave_temp')
mpl.show()