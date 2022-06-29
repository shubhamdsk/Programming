# 

import os
PATH = 'C:\\Users\\shubham Deshmukh\\Desktop\\College\\Python\\Programming\\Data Science'
fileCount = 0 
dirCount = 0
for root,dirs,files in os.walk(PATH):
    print('Looking in :',root)
    for directories in dirs:
        dirCount +=1
    for Files in files:
        fileCount +=1
        
print('No of Files : ',fileCount)
print('No of Directories : ',dirCount)
print('Total',(dirCount+fileCount))