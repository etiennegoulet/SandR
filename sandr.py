#%%
import os
import sys
import shutil
import pandas as pd
from pandas import read_html
import re
import markdown

input_folder_path = "/Users/etienne.goulet/Documents/Python Projects/sandr final/input" 
output_folder_path = os.path.join(os.path.dirname(input_folder_path), "output")
#input_folder_path = input("Please enter your input folder path: ")
#output_folder_path = input("Please enter your output folder path: ")
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

df = pd.read_csv('/Users/etienne.goulet/Documents/Python Projects/sandr final/inoutconfig.csv')
#input = df['Input'].tolist() # input list

re_match=df['Match'].tolist() # regex match list
re_match=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), re_match)) # nan filter

re_replace=df['Replace'].tolist() # regex replace 
re_replace=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), re_replace)) # nan filter


for file_name in os.listdir(input_folder_path):
    if file_name.endswith(".html") or file_name.endswith(".md"): #HTML IMPORT AND SEARCH AND REPLACE
        file_path = os.path.join(input_folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            html_string = f.read()
            #for i, o in zip(input,output):     #replace element 1 of input by element 1 of output
            #    html_string = html_string.replace(i,o)
            for u, p in zip(re_match,re_replace):     #regex replace
                html_string = re.sub(u,p,html_string,count=0)
        base_name, ext = os.path.splitext(file_name)
        new_file_name = base_name + ext
        new_file_path = os.path.join(output_folder_path, new_file_name)
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(html_string)
    #if file_name == base_name + "_files":
        #dir_name = base_name +"_files"
        #shutil.copytree(os.path.join(input_folder_path, file_name), os.path.join(output_folder_path, dir_name))

print("Thank you and have a good day!")

