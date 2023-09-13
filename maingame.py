healthp = 0
actionp = 0
armorp = 0
damagep = 0

file = open("dialogue_name.txt")
content = file.readlines()

usern = input(content[0])
playern = print(content[1], usern)

with open("savedata.txt", "r") as f:
    f.write(f"{healthp}\n")
    f.write(f"{actionp}\n")
    f.write(f"{armorp}\n")
    f.write(f"{damagep}\n")
    f.write(str(usern))

file = open("dialogue_start.txt")
content = file.readlines()