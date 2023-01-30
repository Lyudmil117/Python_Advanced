def words_sorting(*data):
    words = {}
    to_print = []
    for word in data:
        if word not in words:
            words[word] = sum([ord(x) for x in word])

    all_values = sum([x for x in words.values()])

    if all_values % 2 == 0:
        sort = sorted(words.items(), key=lambda x: x[1])
        for item in sort:
            to_print.append(f'{item[0]} - {item[1]}')
        return "\n".join(to_print)
    else:
        sort = sorted(words.items(), key=lambda x: -x[1])
        for item in sort:
            to_print.append(f'{item[0]} - {item[1]}')
        return "\n".join(to_print)


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))