import csv

f_obj = open ("data.csv")
reader = csv.reader(f_obj)
for line in reader:
    print(line)