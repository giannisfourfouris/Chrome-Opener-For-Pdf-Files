import os

dirpath = os.getcwd()
import subprocess

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
path = dirpath
import sys

fileList = os.listdir(path)

count = 0
for file in fileList:
    stringfile = path + "\ ".strip() + file;
    suffix = ".pdf"
    if (file != "ΣΗΜΕΙΩΣΕΙΣ ΠΙΘΑΝΟΤΗΤΩΝ.pdf" and file != "hw 2018-2019.pdf" and file.endswith(suffix)):
        p = subprocess.Popen([chrome_path, stringfile])
        count = count + 1;
if (count == 0):
    print("This directory has not pdf files!")
else:
    print("Everything works Great!")
os.system("PAUSE")