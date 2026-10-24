def main():
    emoticon = input("Emoticons to emojis:")
    print(faces(emoticon))


def faces(emoji):
    
   return emoji.replace(":)", "😊").replace(":(", "😢").replace(":D", "😄").replace(":'(", "😭").replace("XD", "😆").replace(":/cls", "😕").replace(":P", "😛").replace(";)", "😉").replace(":O", "😮").replace("<3", "❤️")

main()