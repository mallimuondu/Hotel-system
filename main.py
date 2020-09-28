from daterbase import *
now = time.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour >= 12 and hour <= 18:
    print("Good afternoon")         
elif hour > 18 and hour < 19: 
    print("Good evening")
else:
    print('Have a nice night.')

def cheking():
    def new_not():
        b = input('''are you:
        a.new
        b.not new
        ''')
        if b == 'a':
            d = input('hello what is your first name:')
            a = input('how many days are you staying:')
            print('WELCOME '+d+' you are staing for '+a+' days')
            d = input('''
            WE HAVE 4 TYPES OF ROOMS
            a.single room 1-10-5000
            b.double room 11 - 20-10000
            d.family room 21-30-15000
            e.king/queen room 31 - 35-25000
            ''')
            if d == 'a':
                print('these are the avalable rooms')
                def read():
                    c.execute('SELECT * from single_rooms')
                    print(c.fetchall())
                read()


                def Delete():
                    n = input('choose the room you want:')
                    c.execute("DELETE FROM single_rooms WHERE roomnumber=?", (n,))
                    conn.commit()
                Delete()
                c.execute('INSERT INTO billing(bill)VALUES(5000)')
                conn.commit()
#                    c.execute('select * from rooms')
#                    print(c.fetchall())
            elif d == 'b':
                print('these are the avalable rooms')

                c.execute('select * from duble_rooms')
                print(c.fetchall())


                def Delete1():
                    n = input('choose the room you want:')
                    c.execute("DELETE FROM duble_rooms WHERE roomnumber=?", (n,))
                    conn.commit()
                Delete1()                
                n = 10000
                total += n
                c.execute('INSERT INTO billing(bill)VALUES(10000)')
                conn.commit()
            elif d == 'd':
                print('these are the avalable rooms')

                c.execute('select * from family_rooms')
                print(c.fetchall())


                def Delete2():
                    n = input('choose the room you want:')
                    c.execute("DELETE FROM family_rooms WHERE roomnumber=?", (n,))
                    conn.commit()
                Delete2()
                n = 5000
                total += n
                c.execute('INSERT INTO billing(bill)VALUES(15000)')
                conn.commit()
            elif d == 'e':
                print('these are the avalable rooms')

                c.execute('select * from king_queen_room')
                print(c.fetchall())


                def Delete2():
                    n = input('choose the room you want:')
                    c.execute("DELETE FROM king_queen_room WHERE roomnumber=?", (n,))
                    conn.commit()
                Delete2()
                c.execute('INSERT INTO billing(bill)VALUES(25000)')
                conn.commit()
        elif b == 'b':
            print('WELCOME')
        else:
            print('i do not understund you')
    new_not()
    def what_do_want_todo():
        print('what do you want  to do')
        e = input('''
        a.go to the swiming pool area
        b.go to eating area
        d.go to the movie area
        e.go to the gaming area
        f.go to the ocean area
        g.go to the gym area
        h go to your room
        WHERE DO YOU WANT TO GO
        :
        ''')
        if e == 'a':
            def pool():
                f = input('''
                a.go to the swiming pool
                b.go to the water slide
                c.go to the water park    
                ''')
                if f == 'a':
                    print('ready to dive')
                    h = input("(yes,no):")
                    if h == 'yes':
                        import time
                        print('3')
                        time.sleep(0.5)
                        print('2')
                        time.sleep(0.5)
                        print('1 DIVE')
                    elif h == 'no':
                        print('ok then enter the pool')
                elif f == 'b':
                    import time
                    print('climb the stars')
                    time.sleep(3)
                    print('3')
                    time.sleep(0.5)
                    print('2')
                    time.sleep(0.5)
                    print('1 push')
                    print('sliding ..')
                    time.sleep(2)
                    print('you are in the water')
                g = input('had fun at the pool area.do you want to do anithing else  y or n:')
                if g == 'y':
                    what_do_want_todo()
                else:
                    print('then you can go to you room')
            pool()    
        elif e == 'b':
            def eating():
                z = input(''' WHAT ARE you eating:
                a.breackfirst
                b.lunch
                c.desert
                d.dinner
                ''')
                if z == 'a':
                    def breackfirst():
                        a = input('''
                        WE HAVE:
                        a.tost
                        b.egg
                        d.sausage
                        e.black tea
                        f.tea
                        g.drinking chocklet
                        h.pancakes
                        ''')
                        if a == 'g':
                            d = input('''
                            YOU WANT IT WITH
                            a.honey
                            b.choclet
                            d.icing suger
                            THAT IS 10 FOR ANY PLUS THE PANCKEC
                            ''')
                            c.execute('INSERT INTO billing(bill)VALUES(10)')
                            conn.commit()
                        elif a == 'a':
                            print('that is 5 for 1 tost bread')
                            c.execute('INSERT INTO billing(bill)VALUES(5)')
                            conn.commit()
                        elif a == 'b':
                            print('that is 2 for 1 tost bread')
                            c.execute('INSERT INTO billing(bill)VALUES(2)')
                            conn.commit()
                        elif a == 'd':
                            print('that is 10 for 1 sosage')
                            c.execute('INSERT INTO billing(bill)VALUES(10)')
                            conn.commit()
                        elif a == 'e':
                            print('that is 40 for 1 cup')
                            c.execute('INSERT INTO billing(bill)VALUES(40)')
                            conn.commit()
                        elif a == 'f':
                            print('that is 50 for 1 cup')
                            c.execute('INSERT INTO billing(bill)VALUES(50)')
                            conn.commit()
                        elif a == 'f':
                            print('that is 40 for 1 cup')
                            c.execute('INSERT INTO billing(bill)VALUES(40)')
                            conn.commit()

                        h = input('you want to do anithing else  y or n:')
                        if h == 'y':
                            what_do_want_todo()
                        else:
                            pass
                    breackfirst()
                elif z == 'b':
                    def lunch():
                        d = input('''
                        WE HAVE:
                        a.chips and somthing else
                        b.chiken
                        d.pizza
                        e.githeri
                        f.rice
                        ''')
                        if d == 'a':
                            print('that is 60 for 1 plate of chips and one of any')
                            c.execute('INSERT INTO billing(bill)VALUES(60)')
                            conn.commit()
                        elif d == 'b':
                            print('that is 960 for a hole chiken')
                            c.execute('INSERT INTO billing(bill)VALUES(960)')
                            conn.commit()
                        elif d == 'd':
                            print('that is 900 for a hole lage pizza')
                            c.execute('INSERT INTO billing(bill)VALUES(900)')
                            conn.commit()
                        elif d == 'e':
                            print('that is 80 for a plate')
                            c.execute('INSERT INTO billing(bill)VALUES(80)')
                            conn.commit()
                        elif d == 'f':
                            print('that is 100 for a plate')
                            c.execute('INSERT INTO billing(bill)VALUES(960)')
                            conn.commit()
                    lunch()
                elif z == 'c':
                    def desert():
                        a = input('''
                        a.iscream
                        b.panckeck
                        d.soda
                        ''')
                        if a == 'a':
                            print('that is 400 for one caontainer')
                            c.execute('INSERT INTO billing(bill)VALUES(400)')
                            conn.commit()
                        elif a == 'b':
                            print('that is 10 for two pancakes')
                            c.execute('INSERT INTO billing(bill)VALUES(10)')
                            conn.commit()
                        elif a == 'd':
                            print('that is 40 for one bottle')
                            c.execute('INSERT INTO billing(bill)VALUES(960)')
                            conn.commit()
                    desert()
                elif z == 'd':
                    def dinner():
                        d = input('''
                        WE HAVE:
                        a.chips and somthing else
                        b.chiken
                        d.pizza
                        e.githeri
                        f.rice
                        ''')
                        if d == 'a':
                            print('that is 60 for 1 plate of chips and one of any')
                            c.execute('INSERT INTO billing(bill)VALUES(60)')
                            conn.commit()
                        elif d == 'b':
                            print('that is 960 for a hole chiken')
                            c.execute('INSERT INTO billing(bill)VALUES(960)')
                            conn.commit()
                        elif d == 'd':
                            print('that is 900 for a hole lage pizza')
                            c.execute('INSERT INTO billing(bill)VALUES(900)')
                            conn.commit()
                        elif d == 'e':
                            print('that is 80 for a plate')
                            c.execute('INSERT INTO billing(bill)VALUES(80)')
                            conn.commit()
                        elif d == 'f':
                            print('that is 100 for a plate')
                            c.execute('INSERT INTO billing(bill)VALUES(960)')
                            conn.commit()
                    dinner()
                g = input('had a nice meal.do you want to do anithing else  y or n:')
                if g == 'y':
                    what_do_want_todo()
                else:
                    print('then you can go to you room')
            eating()
        elif e == 'd':
            def thieta():
                g = input(''' WHICH Movie are you watching:
                a.The Karate Kid 
                b.The Incredibles
                d.The main ivent
                ''')
                a = input('do you want anithing like soda or popcorn: ')
                if a == 'yes':
                    b = input('what do you want soda or popcorn or both: ')

                    if b == 'soda':
                        print('ok')
                    elif b =='popcorn':
                        print('ok')
                    elif b == 'both':
                        print('ok')
                elif a == 'no':
                    pass
                g = input('enjoyed the movei .do you want to do anithing else  y or n:')
                if g == 'y':
                    what_do_want_todo()
                else:
                    print('then you can go to you room')
            thieta()
        elif e == 'e':
                g = input(''' WHICH game are you playing:
                a. pool
                b.table tennis
                d.vr kit
                ''')
                g = input('enjoyed the game .do you want to do anithing else  y or n:')
                if g == 'y':
                    what_do_want_todo()
                else:
                    print('then you can go to you room')
        elif e == 'f':
                g = input(''' WHAT DO YOU WANT TO DO:
                a. swim
                b.stay on sand and bild
                ''')
                if g == 'a':
                    print('lets go')
                    import time
                    time.sleep(2)
                    print('here is a big waive')
                g = input('enjoyed your self at the beach. make shure you take a chower befor entering .do you want to do anithing else  y or n:')
                if g == 'y':
                    what_do_want_todo()
                else:
                    print('then you can go to you room')           
        elif e == 'g':
                g = input(''' WHAT DO YOU WANT TO DO:
                a. weghts
                b. tredmill
                ''')
                g = input('enjoyed your self at the gym. do you bild musos .do you want to do anithing else  y or n:')
                if g == 'y':
                    what_do_want_todo()
                else:
                    print('then you can go to you room')                        




        a = input('do you want a bill (y/n)')
        if a == 'y':
            def total():
                print("your total is ")
                global autput
                autput = 0
                b = [c for charging in c.execute('SELECT * FROM billing') for c in charging]
                d = sum(b)
                print(d)
                autput += d



            total()

            def paying():
                a = int(input('pls pay(pay more or equal):'))
                if a > autput:
                    print('your channge is:')
                    d = a - autput 
                    print(d)

                else:
                    print('good bye')
            paying()
        elif a == 'n':
            cheking()
    what_do_want_todo()        
cheking()    