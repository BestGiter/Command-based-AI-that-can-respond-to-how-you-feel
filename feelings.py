from textblob import TextBlob; print("Ok thats good" if (s := TextBlob(input("welcome to this python game\nhow are you\n")).sentiment.polarity) > 0 else "Hope you have a better day" if s < 0 else "Its fine to just be ok")

