#%%
import os
import sys
import shutil
import pandas as pd
from pandas import read_html
import re
import markdown
import argparse

# Find the directory path of the 'sandr.py' file
dir_path = os.path.dirname(os.path.abspath(__file__))

# Set the absolute input folder path and base inoutconfig.csv file in the 'sandr' directory
abs_input_folder_path= os.path.join(dir_path, "input") 
config_path= os.path.join(dir_path,"inoutconfig.csv") 

# Set up the command line argument parser
parser = argparse.ArgumentParser(description='Description of your program')

# Define the 'input_path' and 'config_path' command line for specifying the input folder path and the configuration file path
parser.add_argument('-input', '--input_path', type=str, default=abs_input_folder_path, help='Path to input file')
parser.add_argument('-config', '--config_path', type=str, default=config_path, help='Path to config file')
args = parser.parse_args()

#Get the paths from the command line arguments
input_folder_path = args.input_path
config_path = args.config_path 


output_folder_path = os.path.join(os.path.dirname(input_folder_path), "output")

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Read the configuration file 
df=pd.read_csv(config_path)

# Create lists with items in the specified columns ('Match', 'Replace', 'Type')
re_match=df['Match'].tolist() # regex match list
re_match=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), re_match)) # nan filter

re_replace=df['Replace'].tolist() # regex replace 
re_replace=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), re_replace)) # nan filter

value_type=df['Type'].tolist()
value_type=list(filter(lambda x: (str(x) != 'nan' and str(x) != ''), value_type))

# Iterate over the files in the input folder
for file_name in os.listdir(input_folder_path):
    #If file HTML or Markdown, open
    if file_name.endswith(".html") or file_name.endswith(".md"): 
        # Get the file path
        file_path = os.path.join(input_folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read the file content as a string
            doc_string = f.read()
            # Iterate over the regex match, replace and value type lists
            for u, p, l in zip(re_match,re_replace,value_type):     
                # Perform search and replace based on the value type
                if l.lower() == "string":
                    doc_string= doc_string.replace(u,p)
                elif l.lower() == "regex":
                    doc_string = re.sub(u,p,doc_string,count=0)
        # Get base name and extension of file, and create a new file name with the same base name and extension
        base_name, ext = os.path.splitext(file_name)
        new_file_name = base_name + ext
        # Create the path to the new file in the output folder
        new_file_path = os.path.join(output_folder_path, new_file_name)
        with open(new_file_path, 'w', encoding='utf-8') as f:
            # Write the modified HTML or markdown string to the new file
            f.write(doc_string)


print("All files succesfully processed.")

