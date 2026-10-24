def main():
    chat = input("Enter the conversation to put into indoor language: ")
    print(indoor(chat))

def indoor(subj):
    return subj.lower()



main()