import os
import psutil
import sqlite3


def clear_google_history(term):
    if "chrome.exe" in (p.name for p in psutil.process_iter()):
        os.system("taskkill /im chrome.exe /f")
    

    conn = sqlite3.connect("C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    cr = conn.cursor()
    id = 0
    run = True

    while run:
        run = False
        ids = []

        for rows in cr.execute("SELECT id, url FROM urls where url LIKE '%" + term + "%'"):
            print(rows)

            id = rows[0]
            ids.append((id, ))
        # conn.close()

        cr.executemany("DELETE FROM urls where id = ?", ids)
        conn.commit()
        conn.close()
        
term = input("enter a term: ")
clear_google_history(term)




