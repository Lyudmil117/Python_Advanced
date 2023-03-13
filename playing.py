def start_playing(obj):
    return obj.play()

class Guitar:
    def play(self):
        return "Playing the guitar"

class Children:
    def play(self):
        return "Children are playing"
    #това тък не е към задачата, но ако напишем child = Children() , а после извикаме print(child.start_playing)
    #ще се изпълни пак с тази функция без проблем

guitar = Guitar()
print(start_playing(guitar))