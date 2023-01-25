
li=["you travelled in your summer vacation "]
print('Choose a character:-')
print('boy-press 1')
print('girl-press 2')
print('if no prefrences choose any option.')
character=int(input("character:"))
name=input('name:')
print('~~you are', name,'~~')
if character==2:
    print('''    
                 @@@@
                @@@@@@
                @ . . @
                @  -  @
                @ ### @
                  ###
                  ###
                  ''')
elif character==1:
    print('''
            @@@@@
            @@@@@
             . . 
              -  
             ### 
             ###
             ###
    ''')

#2
print("Choose a place you would like to visit.")
print("mountain press-11")
print("Island press-12")
place=int(input("Destination:"))
if place ==11:
    print('You choose mountain.')
    li.append('you were going to visit mountains.')
    print('''Now choose your mode of transport.
        Car press-1
        Train press-2
        Airplane press-3
        Cycle press-4
        ''')
    trans=int(input("mode of transport: "))
    if trans==1:
        print('You choose Car')
        print('you Die due to landslide.')
        li.append('You travelled by car,and died due to landslide.')

    elif trans==2:
        print('You choose Train')
        print('you reached your destination.')
        li.append('You travelled by car and reached your destination.')
        print('''
              Hotel 1 (has warm water but not bed)-press 1
              Hotel 2(has cold water but nice bed)-press 2
                ''')
        hotel=int(input('Hotel: '))
        if hotel==1:
            print("you chose Hotel 1 (has warm water but not bed)")
            li.append('you stayed in Hotel 1 which had warm water but did not have bed.')
            print("you saw nice mountains and went home.")
            li.append('you saw nice mountains and went home.')
        elif hotel==2:
            print("you chose Hotel 2 (has cold water but nice bed)")
            li.append('you stayed in Hotel 2 which had cold water but had nice bed.')
            print("you ended up going to hospital due to bathing with cold water.")
            li.append("you ended up going to hospital due to bathing with cold water.")
    elif trans==3:
        print('You choose Airplane')
        print('!!!Your plane was hijacked and you died.')
        li.append('you travelled by airplane and your plane was hijacked.you eventually died.')

    elif trans==4:
        print('You choose Cycle')
        print('You reached your destination.')
        li.append('You travelled by cycle and reached your destination.')
        print('''
                      Hotel 1 (has warm water but not bed)-press 1
                      Hotel 2(has cold water but nice bed)-press 2
                        ''')
        hotel = int(input())
        if hotel == 1:
            print("you chose Hotel 1 (has warm water but not bed)")
            li.append('you stayed in Hotel 1 which had warm water but did not have bed.')
            print("you saw nice mountains and went home.")
            li.append('you saw nice mountains and went home.')
        elif hotel == 2:
            print("you chose Hotel 2 (has cold water but nice bed)")
            li.append('you stayed in Hotel 2 which had cold water but had nice bed.')
            print("you ended up going to hospital due to bathing with cold water.")
            li.append("you ended up going to hospital due to bathing with cold water.")
elif place==12:
    print('You choose Island')
    li.append('You went to Island.')
    print('''Now choose your mode of transport.
            Airplane press-1
            Ship press-2
            Boat press-3
            ''')
    trans = int(input("Mode of transport: "))
    if trans == 1:
        print('You choose Airplane')
        li.append('you travelled by Airplane.')
        print('''
        Choose island:
    Island 1🏝(contain dinosaur but you have AK47🔫)-press 1
    Island 2🏝(no food and shelter only one coconut tree)-press 2
        ''')
        island=int(input("island: "))
        if island == 1:
            print("you chose Island 1🏝(contain dinosaur but you have AK47🔫)")
            print("!!!You meet a dinosaur 🦕 and you forgot to load your gun 🔫 in hurry and you die.")
            li.append("you went to an island that had dinosaur but you had AK47🔫.")
            li.append("You were in hurry that you forgot to load your gun and met a dinosaur.the dinosaur ate you.")
        if island == 2:
            print("you chose Island 2🏝(no food and shelter only one coconut tree)")
            print('''
            You choose Island 2🏝
            You survived 3 days then a helicopter 🚁 reached there,
            and save your life and you reach home 🏡.
            ''')
            li.append("you choose Island 2🏝")
            li.append("You survived 3 days using cocunuts and then a helicopter 🚁 reached there.")
            li.append("You came back home 🏡.")
    elif trans == 2:
        print('You chose Ship')
        print('!!!big Thunderstorm.You die in a shipwreck by drowning...')
        li.append('you travelled by a big ship and drowned due to shipwreck caused by a big storm.')
    elif trans == 3:
        print('You choose Boat')
        li.append('You travelled by Boat.')
        print('''
                Choose island:
            Island 1🏝(contain dinosaur but you have AK47🔫)-press 1
            Island 2🏝(no food and shelter only one coconut tree)-press 2
                ''')
        island = int(input())
        if island == 1:
            print("you chose Island 1🏝(contain dinosaur but you have AK47🔫)")
            print("!!!You meet a dinosaur 🦕 and you forgot to load your gun 🔫 in hurry and you die.")
            li.append("you went to an island that had dinosaur but you had AK47🔫.")
            li.append("You were in hurry that you forgot to load your gun and met a dinosaur.the dinosaur ate you.")
        elif island == 2:
            print("you chose Island 2🏝(no food and shelter only one coconut tree)")
            print('''
                    You choose Island 2🏝
                    You survived 3 days then a helicopter 🚁 reached there,
                    and save your life and you reach home 🏡.
                    ''')
            li.append("you choose Island 2🏝")
            li.append("You survived 3 days using cocounut and then a helicopter 🚁 reached there.")
            li.append("You came back home 🏡.")
else:
    print('error')

print('~~~***GaMe End***~~~')
print("Your story:")
for i in li:
    print(i)

