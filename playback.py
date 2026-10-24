
def main():
    talk = input("Enter the text to convert to playback format: ")
    print(playback(talk))

def playback(lect):

    return lect.replace(" ", "...")

main()