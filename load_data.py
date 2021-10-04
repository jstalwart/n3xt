# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:50:56 2021

@author: arnau
"""

import os
import json
import csv
folder = "C:/Users/arnau/Desktop/Feina/N3xt sport7/Feina inicial/open-data-master/events"
content = os.listdir(folder)


shots = []

for file_name in content:
    with open(folder+'/'+file_name, encoding = "utf-8") as file:
        file_data = (json.load(file))
        for event in file_data:
            if event["type"]["id"] == 16:
                X = event["location"][0]
                Y = event["location"][1]
                if event["shot"]["outcome"]["id"] == 97:
                    goal = 1
                else:
                    goal = 0
                shots.append({"goal":goal, "X":X, "Y":Y})                
    
print("Finished loading")
print("Charging data into csv")    

with open("data.csv", mode = "w") as csv_file:
    variables = ["goal", "X", "Y"]
    writer = csv.DictWriter(csv_file, fieldnames = variables)
    writer.writeheader()
    for case in shots:
        writer.writerow(case)

print("Finished charge")