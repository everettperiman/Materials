import pandas as pd
import csv
csv_file = "hkl_vals.txt"
val_list = []
lambda_val = 0
n_val = 1
with open(csv_file, newline='') as csvfile:
    row_reader = csv.reader(csvfile, delimiter=',')
    
    for row in row_reader:
        row_list = []
        for item in row:
            row_list.append(item)
            if item.isnumeric():
                item_string = list(item)
                item_sum = 0
                for number in item_string:
                   item_sum += pow(int(number),2)   
                item_sqrt = pow(item_sum,.5)
                item = item_sqrt
                row_list.append(item)
        val_list.append(row_list)

with open("hkl_output.txt",'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for index,items in enumerate(val_list):
        # spamwriter.writerow(old_list[index])
        spamwriter.writerow(val_list[index])
        