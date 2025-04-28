#My python game
print("welcome to this python game\nhow are you")
answer = input()
possibilities = {
    "good": 1,
    "great": 1,
    "fantastic": 1,
    "wonderful": 1,
    "ok": 0,
    "okay": 0,
    "average": 0,
    "neutral": 0,
    "meh": 0,
    "bad": -1,
    "terrible": -1,
    "amazing": 1,
    "i want to die": -1,
    "awful": -1,
    "could not be worse": -1,
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
        print("Hope you have a better day")
    if feeling == 0:
        print("Its fine to just be ok")
    if feeling > 0:
        print("Ok thats good")
        

