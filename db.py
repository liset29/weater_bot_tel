import sqlite3

con = sqlite3.connect("teleg_database.db")
cur = con.cursor()
lst=[]
def date_base(id_chat,surname,message):
    if id_chat not in lst:
        name="пукич"
        lst.append(id_chat)
        cur.execute(f"INSERT INTO users (id_chat,surname,name) VALUES({id_chat},\"{surname}\",\"{name}\")")
    
    cur.execute(f"INSERT INTO users_mess (id_chat,message) VALUES({id_chat},\"{message}\")")
    
    
    con.commit()
