#!/usr/bin/python3

import os
import sys
from distutils.dir_util import copy_tree
import shutil
import subprocess

directory = os.path.dirname(os.path.abspath(sys.argv[0]))
for directory in os.listdir(directory):
    dirName = os.fsdecode(directory)
    if(os.path.isdir(dirName)):
        print("\t\033[1m"+dirName+"\033[0m")
        shutil.copyfile("Makefile", dirName + "/Makefile")
        os.chdir(dirName)
        try: 
            os.mkdir("Results")
        except FileExistsError:
            print("Results Folder already exists")

        make_process = subprocess.Popen("make", stderr=subprocess.STDOUT)
        if make_process.wait() != 0:
            print("Makefile Crashed!")

        os.chdir('../')
