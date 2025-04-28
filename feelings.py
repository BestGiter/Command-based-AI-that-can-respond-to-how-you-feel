#My python game
print("welcome to this python game\nhow are you")
answer = input()
possibilities = {
    "good": 1,
    "ok": 0,
    "bad": -1,
    "terrible": -1,
    "amazing": 1,
    "fine": 0,
    "well": 1,
}
feeling = None
negate = 0
for items in answer.split(" "):
    if items == "not":
        negate = 1-negate
    if items in possibilities:
        feeling = (feeling+possibilities[items])/2 if feeling != None else possibilities[items]
result = feeling if negate==0 else -feeling
if feeling == None:
    print("you didn't say one of the keywords:")
    for keys in possibilities:
        print(keys+",")
    print("and not")
else:
    if feeling < 0:
        print("Hope you have a better day meow :3")
    if feeling == 0:
        print("Its fine to just be ok meow :3")
    if feeling > 0:
        print("Ok thats good meowwwwww :33")
        

