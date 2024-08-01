def main():

    text_emo = input()
    text_emoji = convert(text_emo)
    print(text_emoji)


def convert(con_text):
    con_text = con_text.replace(":)", "🙂")
    con_text = con_text.replace(":(", "🙁")
    return con_text


main()
