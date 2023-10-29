temp_list = []
f_obj = open("data.csv")
header = f_obj.readline()
for line in f_obj:
    columns = line.split(",")
    if len(columns) >= 10:
        temp_list.append(columns[9])
print(temp_list)
list_of_numbers = []
for temp in temp_list:
    number = float(temp.replace('"',""))
    list_of_numbers.append(number)
print(list_of_numbers)