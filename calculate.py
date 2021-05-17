
import csv
from collections import Counter
with open('C:/Users/dell/Desktop/Python/calculate.py/SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(float(num))
#Mean
n=len(newdata)
total=0
for i in newdata:
    total+=i

mean=total/n
print(str(mean))
#Median
newdata.sort()
if n % 2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=newdata[n//2]
print("medianis"+str(median))
#mode
data=Counter(newdata)
mode_data_for_range = { "85-115": 0, "115-135": 0, "135-160": 0 }

for height, occurence in data.items():
    if 85 < float(height) <   115:
        mode_data_for_range["85-115"] += occurence 
    elif 115 < float(height) < 135:
         mode_data_for_range["115-135"] += occurence
    elif 135 < float(height) < 160:
         mode_data_for_range["135-160"] += occurence
mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]),  int(range.split("-")[1])],occurence 
mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")
