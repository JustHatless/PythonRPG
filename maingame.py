healthp = 0
actionp = 0
armorp = 0
damagep = 0
gold = 0
story = 0

file = open("dialogue_name.txt")
content = file.readlines()

usern = input(content[0])
playern = print(content[1], usern)

with open("savedata.txt", "r") as f:
    f.write(f" {healthp}\n")
    f.write(f" {actionp}\n")
    f.write(f" {armorp}\n")
    f.write(f" {damagep}\n")
    f.write(f" {gold}\n")
    f.write(f" {story}\n")
    f.write(str(usern))
    f.close()

file = open("dialogue_start.txt")
contentst = file.readlines()
answer = ""
print(contentst[21] + usern + content[22])
print(contentst[23])
print(contentst[0])
print(contentst[1])
print(contentst[2])
print(contentst[3])
input(answer)
if input(answer) == contentst[0]:
    story = 1

def talk_5choice():
    print(contentst[24])
    print(contentst[0])
    print(contentst[1])
    print(contentst[2])
    print(contentst[3])
    print(contentst[11])

def talk_6choice():
    print(contentst[24])
    print(contentst[0])
    print(contentst[1])
    print(contentst[2])
    print(contentst[3])
    print(contentst[7])
    print(contentst[11])