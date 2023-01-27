# Clear Browser History

this scripts clears chrome browser history.
the user enters a term and history is deleted based on this terms.
you can also  type all, to delete all history in the browser.

# Dependences.
1. import os.
2. import sqlite3
3. import psutil. ( pip install psutil)

# How it works.
1. first the program checks if chrome is runnig and closes.
2. then connects to history database. since this version is based on windows database file path is stored in 
 db_path = "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
3. 
