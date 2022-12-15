import pandas as pd
import os
import shutil
import zipfile

# ---------------------------->>>>>>>>>>
# please write the name of csv file
path = "test.csv"

# ---------------------------->>>>>>>>>>
# please write the address of source file
# be careful, it should be a zip file
origin ='C:\\VS\\bcs\\data.zip'

data = pd.read_csv(path)

for i in range(len(data)):
    row = data.iloc[i]

    # ---------------------------->>>>>>>>>>
    # please write here the name of columns's head
    name = row["name"]

    # ---------------------------->>>>>>>>>>
    # please write here the name of columns's head
    number = row["sub"]

    target = "{}\\{}".format(name, number)

    # skip this two lines
    # files = os.listdir(origin)
    # for file_name in files:


    shutil.copy(origin,target)
    with zipfile.ZipFile(origin, 'r') as zip_ref:
        zip_ref.extractall(target)
    
    # ---------------------------->>>>>>>>>>
    # please write the name of zip file here
    os.remove(target+"\\data.zip")