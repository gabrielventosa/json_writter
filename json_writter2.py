# coding: utf-8
import os
import json

for root, dirs, files in os.walk(
        'C:/Users/gab_v/AppData/Local/EPS/data/Global_CAE_Standards/'):
    presentation_list =[]
    svgs_iterator = filter(lambda x: x.endswith((".SVG",".svg")), files)
    svgs_list = list(svgs_iterator)
    if len(dirs) > 0:
        for dir in dirs:
              subdir = root+dir
              print()  
              presentation_data = {"Name": dir,
                                   "Creator": "Alejandro Escudero",
                                   "Date": "06/03/2020",
                                   "Version": "1.0",
                                   "DocumentRoot": "./"+dir+"/"}
              presentation_list.append(presentation_data)
        data = {}
        data["Presentations"] = presentation_list
        json_data = json.dumps(data, indent=4)
        print("Writing to file: "+root+"/root.json")
        jsonfile = open(root+"/root.json", "w")
        jsonfile.write(json_data)
        jsonfile.close()
    if len(svgs_list) > 0:
        print("\t\tSub dir: {} SVGs:{} ".format(root+"/"+dir,len(svgs_list)))
        data = {}
        presentation_data = {"slides":len(svgs_list)}
        data["Presentation"] = presentation_data
        json_data = json.dumps(data, indent=4)
        print("Writing to file: "+root+"/presentation.json")
        jsonfile = open(root+"/presentation.json","w")
        jsonfile.write(json_data)
        jsonfile.close()
        
