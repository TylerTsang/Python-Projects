# -*- coding: utf-8 -*-
# Code to run in Python
import zipfile
#Create Zipfile Object in sample.zip to unpack
with zipfile.ZipFile('sample.zip', 'r') as zip_file:
    #Extract to current directory (blank) or specify directory
    zip_file.extractall('directory_to_Unzip_To')
 

    
# Extract File in Command Prompt
# Replace <zipfile> with file to extract
# Replace <output_directory> with desired directory to extract to
#
# Use following code:
# python -e <zipfile> <output_directory>