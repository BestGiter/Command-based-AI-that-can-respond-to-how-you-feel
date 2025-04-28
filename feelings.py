from textblob import TextBlob

user_input = input("welcome to this python game\nhow are you\n")
blob = TextBlob(user_input)

# polarity: -1 (negative) to +1 (positive)
# subjectivity: 0 (objective) to 1 (subjective)
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("Ok thats good")
elif sentiment < 0:
    print("Hope you have a better day")
else:
    print("Its fine to just be ok")
