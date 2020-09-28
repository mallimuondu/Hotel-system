import sqlite3
conn = sqlite3.connect('the.db')
c = conn.cursor()
import time
import datetime as time
import random
def bill_table():
    c.execute('CREATE TABLE IF NOT EXISTS billing( bill INTEGER)')
bill_table() 
def table():
    c.execute('CREATE TABLE IF NOT EXISTS single_rooms(roomnumber INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS duble_rooms(roomnumber INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS family_rooms(roomnumber INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS king_queen_room(roomnumber INTEGER)')
    
def iserting():
    with conn:
        c.execute('INSERT INTO single_rooms VALUES(1)')
        c.execute('INSERT INTO single_rooms VALUES(2)')
        c.execute('INSERT INTO single_rooms VALUES(3)')
        c.execute('INSERT INTO single_rooms VALUES(4)')
        c.execute('INSERT INTO single_rooms VALUES(5)')
        c.execute('INSERT INTO single_rooms VALUES(6)')
        c.execute('INSERT INTO single_rooms VALUES(7)')
        c.execute('INSERT INTO single_rooms VALUES(8)')
        c.execute('INSERT INTO single_rooms VALUES(9)')
        c.execute('INSERT INTO single_rooms VALUES(10)')

        c.execute('INSERT INTO duble_rooms VALUES(11)')
        c.execute('INSERT INTO duble_rooms VALUES(12)')
        c.execute('INSERT INTO duble_rooms VALUES(13)')
        c.execute('INSERT INTO duble_rooms VALUES(14)')
        c.execute('INSERT INTO duble_rooms VALUES(15)')
        c.execute('INSERT INTO duble_rooms VALUES(16)')
        c.execute('INSERT INTO duble_rooms VALUES(17)')
        c.execute('INSERT INTO duble_rooms VALUES(18)')
        c.execute('INSERT INTO duble_rooms VALUES(19)')
        c.execute('INSERT INTO duble_rooms VALUES(20)')

        c.execute('INSERT INTO family_rooms VALUES(21)')
        c.execute('INSERT INTO family_rooms VALUES(22)')
        c.execute('INSERT INTO family_rooms VALUES(23)')
        c.execute('INSERT INTO family_rooms VALUES(24)')
        c.execute('INSERT INTO family_rooms VALUES(25)')
        c.execute('INSERT INTO family_rooms VALUES(26)')
        c.execute('INSERT INTO family_rooms VALUES(27)')
        c.execute('INSERT INTO family_rooms VALUES(28)')
        c.execute('INSERT INTO family_rooms VALUES(29)')
        c.execute('INSERT INTO family_rooms VALUES(30)')

        c.execute('INSERT INTO king_queen_room VALUES(31)')
        c.execute('INSERT INTO king_queen_room VALUES(32)')
        c.execute('INSERT INTO king_queen_room VALUES(33)')
        c.execute('INSERT INTO king_queen_room VALUES(34)')
        c.execute('INSERT INTO king_queen_room VALUES(35)')

    
if __name__=='__main__':
    table() 
    iserting()