from daterbase import *
def insert():
    c.execute('INSERT INTO billing(bill)VALUES(1000)')
    conn.commit()
insert()
def read():
    c.execute('SELECT * FROM billing')
    print(c.fetchall())
    
read()