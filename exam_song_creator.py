def add_songs(*data):
    to_print = []
    songs = {}

    for item in data:
        zaglavie = item[0]
        teksta = item[1]

        if zaglavie not in songs:
            songs[zaglavie] = []

        songs[zaglavie].extend(teksta)

    for song, text in songs.items():
        to_print.append(f"- {song}")
        to_print.extend(text)
    return "\n".join(to_print)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))