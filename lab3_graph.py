import pandas as pd
import matplotlib.pyplot as plt
import csv


low_cutoff = 300
x_offset = 1
y_offset = 10
percent_offset = 1.05

peak_vals = []

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
     temp_list = 
     peak_vals.append(temp_list)
     csv_graph_dict[csv_file_dict[csv_file]] = df

#print the data framep
fig, axs = plt.subplots(4)
for index,key in enumerate(csv_graph_dict.keys()):  
    print(key)
    df = csv_graph_dict[key]
    ax = df.plot(label=key,x="Angle",y="Intensity")
    df.plot.scatter(ax=ax,label="Peaks",x="Angle",y="Peaks",c="orange")
    
    if key is "Grinded Morton Salt" or key is "Morton Salt" or key is "Powder Salt and Al":
        for item in dfb["angle"]:
            ax.axvline(item,linestyle="--",c="green")
        for index,row in dfb.iterrows():
            ax.annotate("{}".format(row["hkl"]),(row["angle"] + x_offset,2000),rotation=45)
    
    if key is "Aluminum Foil" or key is "Powder Salt and Al":
        for item in dfa["angle"]:
            ax.axvline(item,linestyle="--",c="red")
        for index,row in dfa.iterrows():
            # print(row["hkl"])
            ax.annotate("{}".format(row["hkl"]),(row["angle"],2000),rotation=45)

    new_df = df
    new_df.dropna(subset=["Peaks"], inplace=True)
    last_row = 0
    new_df["Angle"] = new_df["Angle"].round(2)
    x_tick_list = []
    for index, row in new_df.iterrows():
        try:
            # print(last_row)
            if row["Angle"] > percent_offset*last_row or last_row == 0:
                x_tick_list.append(row["Angle"])
                # ax.annotate("{0:.2f}".format(row["Angle"]),(row["Angle"] + x_offset,row["Peaks"]+y_offset),rotation=45)
        except:
            pass
        last_row = row["Angle"]
    ax.set_xticks(x_tick_list)
    ax.set_xticklabels(x_tick_list,rotation=45)
    
    fig = plt.gcf()
    fig.savefig("{}.png".format(key),dpi=1000)

# for item in peak_vals:
#     print(item)
#     item.write_csv("peak_output.csv",mode='a')
with open("peak_output",'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    for items in peak_vals:
        spamwriter.writerow(items)
