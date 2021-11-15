import csv
import os 
import os.path as osp
os.chdir('C:\\Users\\Administrator\\Desktop\\COMP6730')
path = ".\covid-data\covid-data"
dirs = os.listdir(path)
dirs.sort()
dirs = dirs[1:]
last_update_file = dirs[-1]
os.chdir('C:\\Users\\Administrator\\Desktop\\COMP6730\\covid-data\\covid-data')
with open(last_update_file) as csvfile:
    reader = csv.reader(csvfile)
    table = [ row for row in reader ]
Q1table = [i[4] for i in table]
Q1table.sort()
#print(table[-2])

print("Question 1:")
print ("Most recent data is in file " + last_update_file)
print("Last updated at "+ Q1table[-2])
confirmed_cases = sum([ int(i[7]) for i in table[1:]])
death_cases = sum([ int(i[8]) for i in table[1:]])
print("Total worldwide cases: " ,confirmed_cases,", Total worldwide deaths: ", death_cases)

import pandas as pd
d14 = pd.read_csv("C:\\Users\\Administrator\\Desktop\\COMP6730\\covid-data\\covid-data\\" + last_update_file)
d14_sum = d14.groupby('Country_Region')['Confirmed','Deaths'].sum()
#d14_sum.to_csv('..\d14.csv')
print("----------")
print("Question 2")
def new_sorted(seq):
    return -int(seq[1])
with open('..\d14.csv') as csvfile:
    reader = csv.reader(csvfile)
    t14 = [ row for row in reader ][1:]
    new_t14 = sorted(t14,key=new_sorted)
    t14 = new_t14[:10]
    country = [ row[0] for row in t14 ]
    death = [ row[1] for row in t14]

d13 = pd.read_csv("C:\\Users\\Administrator\\Desktop\\COMP6730\\covid-data\\covid-data\\09-13-2021.csv")
d13_sum = d13.groupby('Country_Region')['Confirmed','Deaths'].sum()
#d13_sum.to_csv('..\d13.csv')
with open('..\d13.csv') as csvfile:
    reader = csv.reader(csvfile)
    t13 = [ row for row in reader ][1:]
    new_t13 = sorted(t13,key=new_sorted)
    t13 = new_t13[:10]
    country = [ row[0] for row in t13 ]
    death = [ row[1] for row in t13]
for i in range(len(t14)):
    t14[i].append(int(t14[i][1])-int(t13[i][1]))
    
for i in t14:
    print(i[0]+" - total cases: " + i[1] + " deaths: " + i[2] + " new:", i[3])    

count = 0
print("----------")
print("Question 3:")
dirs.reverse()
new_confirm = 0
new_death = 0
c = 0
l_d = 0
for i in dirs:
    count += 1
    with open(i) as csvfile:
        reader = csv.reader(csvfile)
        table = [ row for row in reader ]
        table_confirm = [ row[7] for row in table ]
        table_death =  [ row[8] for row in table ]
        if count >=2:
            cases = new_confirm-sum([ int(i) for i in table_confirm[1:]])
            deaths = new_death - sum([ int(i) for i in table_death[1:]])
            print(l_d[0:10] +": new cases:",cases,"new deaths: ",deaths)
            c+=1
        new_confirm = sum([ int(i) for i in table_confirm[1:]])
        new_death = sum([ int(i) for i in table_death[1:]])
        l_d = i
path_to_files = ".\covid-data\covid-data"
all_records = [pd.read_csv(file_name) for file_name in dirs]
t = [i for i in all_records]       
count = 0
new_confirm = 0
new_death = 0
c = 0
l_d = 0
for i in dirs:
    print(dirs.index(i))
    count += 1
    table = t[dirs.index(i)]
    print(type(table))
    table_confirm = [ row[7] for row in table ]
    table_death =  [ row[8] for row in table ]
    if count >=2:
        cases = new_confirm-sum([ int(i) for i in table_confirm[1:]])
        deaths = new_death - sum([ int(i) for i in table_death[1:]])
        print(l_d[0:10] +": new cases:",cases,"new deaths: ",deaths)
        c+=1
    new_confirm = sum([ int(i) for i in table_confirm[1:]])
    new_death = sum([ int(i) for i in table_death[1:]])
    l_d = i


