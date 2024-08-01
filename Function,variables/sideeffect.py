emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("oh Hi!")


def say(pharase):
    print(pharase + " " + emoticon)


main()
