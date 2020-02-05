import pandas as pd
import matplotlib.pyplot as plt


low_cutoff = 300
x_offset = 1
y_offset = 10
percent_offset = 1.05
csv_file_dict = {"30 90 .03ss 30tps Al Foil.csv":"Aluminum Foil",
                 "30 90 .03ss 30tps Mortan Salt Grinded.csv":"Grinded Morton Salt",
                 "30 90 .03ss 30tps Mortan Salt Grinded+Al powder.csv":"Powder Salt and Al",
                 "30 90 .03ss 30tps Mortan Salt.csv":"Morton Salt"}
csv_file_list, csv_file_names = [], []
[csv_file_list.append(key) for key in csv_file_dict.keys()]
[csv_file_names.append(value for value in csv_file_dict.values())]
#skiprows=1 will skip first line and try to read from second line
csv_graph_dict = {}
dfa = pd.read_csv("al.csv")
dfb = pd.read_csv("nacl.csv")



for csv_file in csv_file_list:
     df = pd.read_csv(csv_file, skiprows=26)
     peaks = df["Intensity"][(df["Intensity"].shift(1) < df["Intensity"]) & (df["Intensity"].shift(-1) < df["Intensity"]) & (df["Intensity"] > low_cutoff)]
     df.insert(1,'Peaks',peaks)
     csv_graph_dict[csv_file_dict[csv_file]] = df