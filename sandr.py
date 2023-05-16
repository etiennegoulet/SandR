#%%
import os
import sys
import shutil
import pandas as pd
from pandas import read_html
import re
import markdown
import argparse

dir_path = os.path.dirname(os.path.abspath(__file__)) # find folder path to directory where sandr.py is set
abs_input_folder_path= os.path.join(dir_path, "input") # set absolute input folder path in sandr final
config_path= os.path.join(dir_path,"inoutconfig.csv") # set config path as the inoutconfig.csv document in the same directory as this program


parser = argparse.ArgumentParser(description='Description of your program')

parser.add_argument('-input', '--input_path', type=str, default=abs_input_folder_path, help='Path to input file')
#parser.add_argument('-output', '--output_path', type=str, help='Path to output file')
parser.add_argument('-config', '--config_path', type=str, default=config_path, help='Path to config file')

args = parser.parse_args()

input_folder_path = args.input_path
#output_path = args.output_path
config_path = args.config_path 

#input_folder_path = "/Users/etienne.goulet/Documents/Python Projects/sandr final/input" 
output_folder_path = os.path.join(os.path.dirname(input_folder_path), "output")
#input_folder_path = input("Please enter your input folder path: ")
#output_folder_path = input("Please enter your output folder path: ")
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

#df = pd.read_csv('/Users/etienne.goulet/Documents/Python Projects/sandr final/inoutconfig.csv')
df=pd.read_csv(config_path)
#input = df['Input'].tolist() # input list
#input=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), input)) # this filters out the nan for all values in list

#output=df['Output'].tolist() # output list
#output=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), output)) # nan filter

re_match=df['Match'].tolist() # regex match list
re_match=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), re_match)) # nan filter

re_replace=df['Replace'].tolist() # regex replace 
re_replace=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), re_replace)) # nan filter

value_type=df['Type'].tolist()
value_type=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), value_type))


for file_name in os.listdir(input_folder_path):
    if file_name.endswith(".html") or file_name.endswith(".md"): #HTML IMPORT AND SEARCH AND REPLACE
        file_path = os.path.join(input_folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            html_string = f.read()
            #for i, o in zip(input,output):     #replace element 1 of input by element 1 of output
            #    html_string = html_string.replace(i,o)
            for u, p, l in zip(re_match,re_replace,value_type):     #regex replace
                if l.lower() == "string":
                    html_string= html_string.replace(u,p)
                elif l.lower() == "regex":
                    html_string = re.sub(u,p,html_string,count=0)
        base_name, ext = os.path.splitext(file_name)
        new_file_name = base_name + ext
        new_file_path = os.path.join(output_folder_path, new_file_name)
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(html_string)
    #if file_name == base_name + "_files":
        #dir_name = base_name +"_files"
        #shutil.copytree(os.path.join(input_folder_path, file_name), os.path.join(output_folder_path, dir_name))

print("All files succesfully processed.")

