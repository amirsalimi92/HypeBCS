import pandas as pd
import os

# ---------------------------->>>>>>>>>>
# please write the name of csv file
path = "test.csv"

data = pd.read_csv(path)
for i in range(len(data)):
    row = data.iloc[i]

    # ---------------------------->>>>>>>>>>
    # please write here the name of columns's head
    name = row["name"]

    # ---------------------------->>>>>>>>>>
    # please write here the name of columns's head
    number = row["sub"]

    if(os.path.exists(name) == False):
        os.makedirs(name)
        print(name)
        os.makedirs(name + "/" + number)
    else:
        if(os.path.exists(name + "/" + number) == False):
            os.makedirs(name + "/" + number)