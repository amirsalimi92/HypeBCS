Hi.
I did two small projects to do faster some normal tasks.

At first, you have to install some libraries to work this code for you.

-Python 3.x
-pandas (pip install pandas)
-shutil (pip install pytest-shutil)
-zipfile (pip install zipfile36)

You can check their docs at https://pypi.org

In the next step, you should insert the name of the folders in a column and subfolders in other columns.
Here we have just one subfolder.

The name of headers in the CSV file is important and you have to edit them in the code in lines 14 & 18 (make_folder.py)
path of the CSV file located in line 6.

***CSV file must be with UTF-8 format with "," delimiter.***
Run the code and you can see all folders and subfolders in the same directory with the code file.

Now in copy_data.py, you have to control the path of CSV file (line8) and the path of the data, that you want to copy
them in all subfolders (line 13) and control again the name of headers with CSV file (lines 22 & 26)
and check the name of the source file in line 41 (It must be like the name of the path file in line 13)

Then run the code and
Enjoy!

Please use the code and give me feedback.
