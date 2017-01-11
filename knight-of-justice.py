import time

inventory = []

print("""





 _   __      _       _     _            __     ___           _   _          _ 
| | / /     (_)     | |   | |          / _|   |_  |         | | (_)        | |
| |/ / _ __  _  __ _| |__ | |_    ___ | |_      | |_   _ ___| |_ _  ___ ___| |
|    \| '_ \| |/ _` | '_ \| __|  / _ \|  _|     | | | | / __| __| |/ __/ _ \ |
| |\  \ | | | | (_| | | | | |_  | (_) | |   /\__/ / |_| \__ \ |_| | (_|  __/_|
\_| \_/_| |_|_|\__, |_| |_|\__|  \___/|_|   \____/ \__,_|___/\__|_|\___\___(_)
                __/ |                                                         
               |___/                                          


        |\                                                              /|     
        | \                                                            / |     
        |  \                                                          /  |     
        |   \                                                        /   |     
        |    \                                                      /    |     
   _____)     \                                                    /     (____ 
   \           \                                                  /          /  
    \           \                                                /          /  
     \           `--_____                                _____--'          /   
      \                  \                              /                 /    
   ____)                  \                            /                 (____ 
   \                       \        /|      |\        /                      / 
    \                       \      | /      \ |      /                      /  
     \                       \     ||        ||     /                      /   
      \                       \    | \______/ |    /                      /    
       \                       \  / \        / \  /                      /     
       /                        \| (*\  \/  /*) |/                       \     
      /                          \   \| \/ |/   /                         \    
     /                            |   |    |   |                           \   
    /                             |\ _\____/_ /|                            \  
   /______                       | | \)____(/ | |                      ______\ 
          )                      |  \ |/vv\| /  |                     (        
         /                      /    | |  | |    \                     \       
        /                      /     ||\^^/||     \                     \      
       /                      /     / \====/ \     \                     \     
      /_______           ____/      \________/      \____           ______\    
              )         /   |       |  ____  |       |   \         (           
              |       /     |       \________/       |     \       |           
              |     /       |       |  ____  |       |       \     |           
              |   /         |       \________/       |         \   |           
              | /            \      \ ______ /      /______..    \ |           
              /              |      \\______//      |        \     \           
                             |       \ ____ /       |LLLLL/_  \                
                             |      / \____/ \      |      \   |               
                             |     / / \__/ \ \     |     __\  /__             
                             |    | |        | |    |     \      /             
                             |    | |        | |    |      \    /              
                             |    |  \      /  |    |       \  /               
                             |     \__\    /__/     |        \/                
                            /    ___\  )  (  /___    \                         
                           |/\/\|    )      (    |/\/\|                        
                           ( (  )                (  ) )


                        
""")

input("""                           Press any Enter to continue...
""")
print()

print("""Welcome to Knight of Justice!  Do you have what it takes to reclaim
your homeland and to seek justice?  Hrothgar, the mighty dragon of old, has
burned your home and killed all of your family.  It's time to right wrongs
and to slay the mighty beast!""")
print()

print("What is your name knight?")
player = input(">>> ")
print()

print("Brave knight Sir " + str.capitalize(player) + ".")
print()
print("What is it you seek, justice or vengeance?")
reason = input(">>> ")
print()

if reason == ("justice"):
    print("""Then justice you will have, but to slay the dragon you will need a mighty arm and
a keen mind.""")

else: 
    print("""Well, obviously you didn't read the title of the game.  Oh well, on with it then.""")
print()

#Beginning Block
def seventeen():
#    print("17: Beginning Block")
    print("""You awake with the whole world around you on fire.  The countryside lay
in ruins.  Hrothgar the mighty dragon has awoken from his slumber and has
destroyed everything you've loved.  You have nothing but the clothes on your
back.  You will have to scavenge for everything you need before tracking the
beast down to his cave in the east in order to slay him.""")
    print()
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        seventeen()
        print()
    
    elif action.lower() == "go north":
        print()
        fourteen()

    elif action.lower() == "go east":
        print("Your way is blocked by a dense, impassable forest.")
        print()        
        seventeen()

    elif action.lower() == "go south":
        print("Your way is blocked by a dense, impassable forest.")
        print()        
        seventeen()

    elif action.lower() == "go west":
        print("Your way is blocked by a dense, impassable forest.")
        print()        
        seventeen()

    else:
        print("Sorry, that isn't possible.")
        print()        
        seventeen()
        
#Forest
def sixteen():
#    print("16: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        sixteen()
    
    elif action.lower() == "go north":
        print("""Are you sure?  Dragons are nasty creatures?  Do you have
everything you need to defend yourself and kill the dragon?""")
        print()
        action = input(">>> ")
        
        if action.lower() == "yes":
            print()
            twelve()
            
        else:
            print()
            sixteen()

    elif action.lower() == "go east":
        print("Your way is blocked by a dense, impassable forest.")
        print()        
        sixteen()

    elif action.lower() == "go south":
        print("Your way is blocked by a dense, impassable forest.")
        print()        
        sixteen()

    elif action.lower() == "go west":
        print()        
        fifteen()

    else:
        print("Sorry, that isn't possible.")
        print()        
        sixteen()
        
#Shop
def fifteen():
#    print("15: Shop")
    print("""You find a nice, small shop that sells various items.  A shopkeeper is sitting
outside.""")
    print()  
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "talk to shopkeeper":
          print("""The shopkeeper says, 'Hi, I'm sorry, but we're running low on supplies today.
I'm still waiting on a delivery.  All I have in stock right now is some
medicine.'""")
          print()
          fifteen()

    elif action.lower() == "buy medicine":
        print()
        
        if "gold" in inventory:
            print("The shopkeeper says, 'That will do!  Here's your medicine.'")
            inventory.append("medicine")
            inventory.remove("gold")
            print()
            fifteen()
            
        else:
            print("""You have no gold to pay for the medicine.  Perhaps you should
find some.""")
            print()
            fifteen()

    elif action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        fifteen()          
    
    elif action.lower() == "go north":
        print()
        eleven()

    elif action.lower() == "go east":
        print()
        sixteen()

    elif action.lower() == "go south":
        print("Your way is blocked by a dense, impassable forest.")
        print()
        fifteen()

    elif action.lower() == "go west":
        print()
        fourteen()

    else:
        print("Sorry, that isn't possible.")
        print()
        fifteen()
        
#Forest            
def fourteen():
#    print("14: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        fourteen()
    
    elif action.lower() == "go north":
        print()
        ten()

    elif action.lower() == "go east":
        print()
        fifteen()

    elif action.lower() == "go south":
        print("There is no reason to return to there.")
        print()
        fourteen()

    elif action.lower() == "go west":
        print()
        thirteen()

    else:
        print("Sorry, that isn't possible.")        
        print()
        fourteen()
    
#Forest
def thirteen():
#    print("13: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        thirteen()
    
    elif action.lower() == "go north":
        print()
        nine()

    elif action.lower() == "go east":
        print()
        fourteen()

    elif action.lower() == "go south":
        print("Your way is blocked by a dense, impassable forest.")      
        print() 
        thirteen()

    elif action.lower() == "go west":
        print("Your way is blocked by a dense, impassable forest.")
        
        print()        
        thirteen()

    else:
        print("Sorry, that isn't possible.")
        
        print()
        thirteen()
        
#Dragon Cave
def twelve():
#    print("Dragon Cave")
#    inventory.append("shield")
#    inventory.append("sword")
    print("12: Dragon Cave")
    print("""Hrothgar, a giant, winged, fire-breathing dragon spreads his wings as he stands, inhales
and then breathes out huge flames of fire at you!""")
    print()
        
    if "shield" not in inventory:
        print("""
                   ...
                 ;::::;
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#

""")
        print("You're dead.  Good job.")
        print()
        print("Play again? Yes or no?")
        print()
        action = input(">>> ")
        
        if action.lower() == "yes":
            print()
            seventeen()
            
        elif action.lower() == "no":
            print()
            print("Goodbye.")
            print()
            
    elif "shield" in inventory and "sword" not in inventory:
        shield_only()
        
    elif "shield" in inventory and "sword" in inventory:
        sword_and_shield()
        
    else:
        print("Sorry, that isn't possible.")
        twelve()
            
#Shield Only
def shield_only():
#    print("Shield Only")
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        shield_only()    
    
    if action.lower() == "block with shield":
        print()
        print("You block Hrothgar's mighty breath with your shield.  He appears vulnerable!")
        print()
        print("But you have no sword!")
        print()     
        print("""While rethinking the wisdom of attacking Hrothgar with no weapon, he
eats you.""")
        print("""
                   ...
                 ;::::;
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#

""")
        print("You're dead.  Good job.")
        print()
        play_again()
    
    else:
        print("Sorry, that isn't possible.")
        print()
        shield_only()
                
#Sword and Shield
def sword_and_shield():
#    print("Sword and Shield")
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        sword_and_shield()
    
    if action.lower() == "block with shield":
        print("You block Hrothgar's mighty breath with your shield.  He appears vulnerable!")
        print()
        print("What do you wish to do?")
        print()
        action = input(">>> ")
        
        if action.lower() == "kill hrothgar with sword":
            print()
            print("""You thrust you blade into the belly of the beast!  He thrashes
around trying to bite you and burn you, but you block all his attempts while driving the sword
deeper into his belly!  With his dying breath Hrothgar says, 'You are victorious.  Justice is done...""")
            print()
            print("You win.")
            print()
            play_again()
                
        elif action.lower() == "kill dragon with sword":
            print()
            print("""You thrust you blade into the belly of the beast!  He thrashes
around trying to bite you and burn you, but you block all his attempts while driving the sword
deeper into his belly!  With his dying breath Hrothgar says, 'You are victorious.  Justice is done...""")
            print("""
          _,.
        ,` -.)
       ( _/-\\-._
      /,|`--._,-^|            ,
      \_| |`-._/||          ,'|
        |  `-, / |         /  /
        |     || |        /  /
         `r-._||/   __   /  /  
     __,-<_     )`-/  `./  /   
    '  \   `---'   \   /  /    
        |           |./  /      
        /           //  /      
    \_/' \         |/  /       
     |    |   _,^-'/  /      
     |    , ``  (\/  /_
      \,.->._    \X-=/^
      (  /   `-._//^`  
       `Y-.____(__}
        |     {__)
              ()
            """)

            print("You win.")
            print()
            play_again()
              
        else:
            print("Sorry, that isn't possible.")
            print()
            sword_and_shield()

#Play Again
def play_again():
#    print("Play Again")
    print("Play again? Yes or no?")
    print()
    action = input(">>> ")
    print()
    if action.lower() == "yes":
        print()
        seventeen()
    elif action.lower() == "no":
        print("Goodbye.")
        print()
    else:
        print("Sorry, that isn't possible.")
        print()
        play_again()

#Forest
def eleven():
#    print("11: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        eleven()
    
    elif action.lower() == "go north":
        print()
        seven()

    elif action.lower() == "go east":
        print("""Are you sure?  Dragons are nasty creatures?  Do you have
everything you need to defend yourself and kill the dragon?""")
        print()
        action = input(">>> ")
        print()
        if action.lower() == "yes":
            print()
            twelve()
        else:
            print()
            eleven()

    elif action.lower() == "go south":
        print() 
        fifteen()

    elif action.lower() == "go west":
        print()        
        ten()

    else:
        print("Sorry, that isn't possible.")
        print()
        eleven()
        
#Forest
def ten():
#    print("10: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        ten()
    
    elif action.lower() == "go north":
        print()
        six()

    elif action.lower() == "go east":
        print()
        eleven()

    elif action.lower() == "go south":
        print()
        fourteen()

    elif action.lower() == "go west":
        print()
        nine()

    else:
        print("Sorry, that isn't possible.")
        print()
        ten()
        
#Burning Castle
def nine():
#    print("9: Burning Castle")
    print("You see the castle burning and in ruins.  There's an elderly man there.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "talk to man":
        print()
        questQuestions()

    elif action.lower() == "talk to elderly man":
        print()
        questQuestions()

    elif action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        nine()

    elif action.lower() == "go north":
        print()
        five()

    elif action.lower() == "go east":
        print()
        ten()

    elif action.lower() == "go south":
        print()
        thirteen()

    elif action.lower() == "go west":
        print("Your way is blocked by a dense, impassable forest.")
        print()
        nine()

    else:
        print("Sorry, that isn't possible.")
        print()
        nine()

## Quest Questions
def questQuestions():
#    print("Quest Questions")
    print("Answer me these questions three!")
    print()
    print("What is your name?")
    print()
    answer1 = input(">>> ")
    print()
    if answer1.lower() == player:
        print("What is your quest?")
        print()
        answer2 = input(">>> ")
        print()
        if answer2.lower() == reason:
            print("How many species of pangolins are there?")
            print()
            answer3 = input(">>> ")
            print()
            if answer3 == "seven":
                print("""The elderly man says, 'You are the chosen one!  Take this sword
and slay the dragon!""")
                print()
                inventory.append("sword")
            else:
                print("Wrong!  Come back later.")
                print()
                nine()
        else:
            print("Wrong!  Come back later.")
            print()
            nine()
    else:
        print("Wrong!  Come back later.")
        print()
        nine()
    nine()

#Forest
def eight():
#    print("8: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        eight()
    
    elif action.lower() == "go north":
        print()
        four()

    elif action.lower() == "go east":
        print("Your way is blocked by a dense, impassable forest.")
        print()
        eight()

    elif action.lower() == "go south":
        print("""Are you sure?  Dragons are nasty creatures?  Do you have
everything you need to defend yourself and kill the dragon?""")
        print()
        action = input(">>> ")
        if action.lower() == "yes":
            print()
            twelve()
        else:
            print()
            eight()

    elif action.lower() == "go west":
        print()
        seven()

    else:
        print("Sorry, that isn't possible.")
        print()
        eight()
        
#Hollow Tree
def seven():
#    print("7: Hollow Tree")
    print("You stand in a meadow with a large tree in the middle.  There is a hole in the tree.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "look in hole":
        print("Someone seems to have left their pickaxe in the tree.")
        print()
        seven()

    elif action.lower() == "get pickaxe":
        print("You reach into the tree and get the pickaxe.")
        inventory.append("pickaxe")
        print()
        seven()
        
    elif action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        seven()
    
    elif action.lower() == "go north":
        print()
        three()

    elif action.lower() == "go east":
        print("You find yourself in a forest with nothing notable around you.")
        print()
        eight()

    elif action.lower() == "go south":
        print()
        eleven()

    elif action.lower() == "go west":
        print()
        six()

    else:
        print("Sorry, that isn't possible.")
        print()
        seven()
        
#Forest
def six():
#    print("6: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        six()
    
    if action.lower() == "go north":
        print()
        two()

    elif action.lower() == "go east":
        print()
        seven()

    elif action.lower() == "go south":
        print()
        ten()

    elif action.lower() == "go west":
        print()
        five()

    else:
        print("Sorry, that isn't possible.")
        print()
        six()
        
#Village
def five():
#    print("5: Village")
    print("""You enter village.  You see a little, old lady that keeps looking at you like
she wants to tell you something.""")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "talk to lady":
        print()
        print("Did you know that there are seven species of pangolin?")
        print()
        five()

    elif action.lower() == "talk to little, old lady":
        print()
        print("Did you know that there are eight species of pangolin?")
        print()
        five()

    elif action.lower() == "inventory":
        print()
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        five()
    
    elif action.lower() == "go north":
        print()
        one()

    elif action.lower() == "go east":
        print()
        six()

    elif action.lower() == "go south":
        print()
        nine()

    elif action.lower() == "go west":
        print("Your way is blocked by a dense, impassable forest.")
        print()
        five()

    else:
        print("Sorry, that isn't possible.")
        print()
        five()
        
#Mine
def four():
#    print("4: Mine")
    print("You come upon an old abandoned mine.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "look in mine":
        print("You see a gold vein.")
        print()
        four()

    elif action.lower() == "mine for gold":
        print()
        
        if "pickaxe" in inventory:
            print("You have attained a piece of gold.")
            inventory.append("gold")
            print()
            four()
            
        else:
            print("""You have nothing to mine the gold with.  Perhaps you should look for
a pickaxe.""")
            print()
            four()

    elif action.lower() == "inventory":
        print()
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        four()
    
    elif action.lower() == "go north":
        print()
        print("Your way is blocked by a dense, impassable forest.")
        print()
        four()

    elif action.lower() == "go east":
        print()
        print("Your way is blocked by a dense, impassable forest.")
        print()
        four()

    elif action.lower() == "go south":
        print()
        eight()

    elif action.lower() == "go west":
        print()
        three()

    else:
        print("Sorry, that isn't possible.")
        print()
        four()
        
#Forest
def three():
#    print("3: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print()
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        three()
    
    elif action.lower() == "go north":
        print()
        print("Your way is blocked by a dense, impassable forest.")
        print()
        three()

    elif action.lower() == "go east":
        print()
        four()

    elif action.lower() == "go south":
        print()
        seven()

    elif action.lower() == "go west":
        print()
        two()

    else:
        print("Sorry, that isn't possible.")
        print()
        three()
        
#Forest
def two():
#    print("2: Forest")
    print("You find yourself in a forest with nothing notable around you.")
    print()
    print()
    print("What do you wish to do?")
    action = input(">>> ")
    print()

    if action.lower() == "inventory":
        print()
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        two()

    elif action.lower() == "go north":
        print()
        print("Your way is blocked by a dense, impassable forest.")
        print()
        two()

    elif action.lower() == "go east":
        print()
        three()

    elif action.lower() == "go south":
        print()
        six()

    elif action.lower() == "go west":
        print()
        one()

    else:
        print("Sorry, that isn't possible.")
        print()
        two()
        
#Farm Field
def one():
#    print("1: Farm Field")
    print("You find a field filled with wheat and a farmer leaning on the fence.")
    print()
    print("What do you wish to do?")
    print()
    action = input(">>> ")
    print()

    if action.lower() == "talk to farmer":
        print()
        print("The farmer says 'I have all this wheat to harvest, but I have a sore hand.'")
        print()
        one()

    elif action.lower() == "give medicine to farmer":
        print()

        if "medicine" in inventory:
            print("""'Thank you!  My hand feels much better now.  Here, take this shield.  I
found it while plowing my field.'""")
            inventory.append("shield")
            inventory.remove("medicine")
            print()
            one()

        else:
            print("You have no medicine.  Perhaps you should buy some?")
            print()
            one()

    elif action.lower() == "inventory":
        print()
        print("You have the following items in your inventory.")
        print()
        print(inventory)
        print()
        one()

    elif action.lower() == "go north":
        print()
        print("Your way is blocked by a dense, impassable forest.")
        print()
        one()

    elif action.lower() == "go east":
        print()
        two()

    elif action.lower() == "go south":
        print()
        five()

    elif action.lower() == "go west":
        print()
        print("Your way is blocked by a dense, impassable forest.")
        print()
        one()

    else:
        print()
        print("Sorry, that isn't possible.")
        print()
        one()
        
seventeen()
