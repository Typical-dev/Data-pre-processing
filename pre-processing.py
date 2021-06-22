import csv
dataset1 = []
dataset2 = []
with open("Data-processing/final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset1.append(row)
with open("Data-processing/dataset_2_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
header1 = dataset1[0]
planet_data1 = dataset1[1:]
header2 = dataset2[0]
planet_data2 = dataset2[1:]
header = header1+header2
planet_data = []
for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)
