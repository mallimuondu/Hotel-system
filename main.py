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
    a = input('''are you are you a:
    a.guest
    b.worker
    :
    ''')
    if a == 'a':
        def new_not():
            b = input('''are you:
            a.new
            b.not new
            ''')
            if b == 'a':
                d = input('hello what is your first name:')
                a = input('how many days are you staying:')
                print('WELCOME '+d+' you are staing for '+a+' days')
                print('you room number is')
                print(random.randint(0,100))
                d = input('here is your room card:')
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
            c.go to the movie area
            d.go to the gaming area
            e.go to the ocean area
            f.go to the gym area
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
                    g = input(''' WHAT ARE you eating:
                    a.breackfirst
                    b.lunch
                    d.dinner
                    ''')
                    g = input('had a nice meal.do you want to do anithing else  y or n:')
                    if g == 'y':
                        what_do_want_todo()
                    else:
                        print('then you can go to you room')
                eating()
            elif e =='c':
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
            elif e == 'd':
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
            elif e == 'e':
                    g = input(''' WHAT DO YOU WANT TO DO:
                    a. swim
                    b.stay on sand and bild
                    ''')
                    g = input('enjoyed your self at the beach. make shure you take a chower befor entering .do you want to do anithing else  y or n:')
                    if g == 'y':
                        what_do_want_todo()
                    else:
                        print('then you can go to you room')           
            elif e == 'f':
                    g = input(''' WHAT DO YOU WANT TO DO:
                    a. weghts
                    b. tredmill
                    ''')
                    g = input('enjoyed your self at the gym. do you bild musos .do you want to do anithing else  y or n:')
                    if g == 'y':
                        what_do_want_todo()
                    else:
                        print('then you can go to you room')                        
                    
        what_do_want_todo()
cheking()