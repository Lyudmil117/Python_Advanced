def age_assignment(*names, **data):
    result = []

    for letter, age in data.items():
        wanted_name = ''
        for name in names:
            if name.startswith(letter):
                wanted_name = name
                break
        result.append(f"{wanted_name} is {age} years old.")

    return "\n".join(sorted(result))