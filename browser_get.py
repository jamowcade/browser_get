import os
import psutil
import sqlite3


def clear_google_history(term):
    if "chrome.exe" in (p.name() for p in psutil.process_iter()):
        os.system("taskkill /im chrome.exe /f")
    conn = sqlite3.connect("C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    cr = conn.cursor()
    id = 0
    run = True
    while run:
        run = False
        ids = []
        if term == "all":
            cr.execute("DELETE FROM urls")
            conn.commit()
            conn.close()
            print("all brownser History is cleared")
        else:
            for rows in cr.execute("SELECT id, url FROM urls where url LIKE '%" + term + "%'"):
                print(rows)

                id = rows[0]
                ids.append((id, ))

            cr.executemany("DELETE FROM urls where id = ?", ids)
            conn.commit()
            conn.close()
            print(f"all data associated with {term} has been deleted")
    
term = input("enter a term or (all) to clear all browser history> ")
clear_google_history(term)




