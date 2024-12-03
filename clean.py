#!/usr/bin/python3

import os
import sys
import zipfile
import py7zr

directory = os.path.dirname(os.path.abspath(sys.argv[0]))
for directory in os.listdir(directory):
    dirName = os.fsdecode(directory)

    if(dirName.endswith('.c')):
       os.makedirs(dirName.split('.c')[0])
       os.rename(dirName, dirName.split('.c')[0] + "/main.c")
       
    if(dirName.endswith(".zip")):
        print("Extracting: " + dirName)
        with zipfile.ZipFile(dirName, "r") as zip_ref:
            zip_ref.extractall(dirName.split(".zip")[0])
    
    if(dirName.endswith(".7z")):
        print("Extracting: " + dirName)
        with py7zr.SevenZipFile(dirName, mode='r') as z:
            z.extractall()
            sys.exit()
            
    #if(os.path.isdir(dirName.split('.c')[0])):
    #    os.rename(dirName, dirName.replace(" ", "_"))
    #    for sourcefile in os.listdir(dirName):
    #        if(sourcefile.endswith(".pdf") == False and 
    #           sourcefile.endswith(".png") == False and
    #           sourcefile != "__MACOSX"):
    #           os.rename(dirName + "/" + sourcefile, 
    #           dirName + "/main.c")
