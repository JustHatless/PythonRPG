hp = 10
ap = 10
arm = 0
atk = 0
slot1 = 00
slot2 = 00
slot3 = 00
slot4 = 00
slot5 = 00
slot6 = 00
slot7 = 00
slot8 = 00 
slot9 = 00
m_invspace = 10
c_invspace = 0
r_encounter = 0
storyline = 0
karma = 0
monster = 0
in_battle = 0
arrows = 0

f = open("savedata.txt", "a")
f.write(hp)
f.write(ap)
f.write(arm)
f.write(m_invspace)
f.write(c_invspace)
f.write(slot1)
f.write(slot2)
f.write(slot3)
f.write(slot4)
f.write(slot5)
f.write(slot6)
f.write(slot7)
f.write(slot8)
f.write(slot9)
f.write(karma)
f.write(storyline)
f.close()

#ending stats and also faction relationshops to be added
#save function to be added as an option after each prompt (for example: entering a jungle, you get the option to save) during combat it is disabled however and only gives you the option to save afterwards defeating the enemy

if r_encounter: 1
monster = range(1, 10)

playername = input("Greetings traveller, what is your name? ")
print(playername, " huh? Not that I don't like it just an interesting choice! Very well then!")

#name easter eggs are planned to be added...

#fallout like stats to be added, skills would range depending on how big each stat id (for example, agility 6 is 55 to the base stat of sneak(not final stat))

opt1 = "Go east"
opt2 = "Go west"
opt3 = "Go north"
opt4 = "Go south"
opt5 = "Open Inventory"
opt6 = "Go inside"
opt7 = "Attack" 
opt8 = "Sneak" #Speaks for itself, usable in battle
opt9 = "Lockpick" #Speaks for itself
opt10 = "Speech" #Special dialogue options, usable in battles to escape battle diplomaticaly
opt11 = "Rest" #Cant use in battles, restores hp and ap 
opt12 = "Unarmed" #Unatmed effectiveness
opt13 = "Melee weapons" #Melee weapon effectiveness
opt14 = "Medicine" #Heal items
opt15 = "Barter" #Trading
opt16 = "Throwing" #Throwing weapon in succesful attack chance
opt17 = "Repair" #Special dialogues and repair prompts
opt18 = "Survival" #More hp and ap in general
opt19 = "Ranged" #Bows


print("Welcome mighty", playername, "on your journey. You're in a giant dark forest. What will you do?")
print(opt1)
print(opt2)
print(opt3)
print(opt4)
print(opt5)

if input() == "east" or "East" or "Look east" or "Look East" or "look East" or "look east":
print('You see a giant cave in front of you. What will you do?')
print("Go inside")
print("Look west")
print("Look south")
print("Look north")
print("Open inventory")

if input() == "west" or "West" or "Look west" or "Look West" or "look West" or "look west":
if r_encounter: 0
print('You see a river, the water looks refreshing. What will you do now', playername + '?')
else:
print('You see a river, however there is a', monster, 'standing there menacingly, eyeing your', slot1, '!')
print(opt7)
print(opt8)
if input() == "attack" or "Fight" or "fight" or "Attack" or "Combat" or "combat":
    print("Choose your weapon to attack with")
    if slot1 = 0:
        print("No item equiped in this slot!")
    else:
        if slot1 = 1 or 2 or 3 or 4 or 5 or 6
        range(1,20) * opt13 / atk
        else:
            if slot1 = 7 or 8 or 9 and arrows != 0
            chance = range(1,20) 
            if chance >= 10
            chance * opt19 / atk
            else:
                print("You tried firing your", slot1,"it was unsuccessful...")
            
    if slot2 = 0: