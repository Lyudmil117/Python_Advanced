def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs['odd'] = [int(x) for x in kwargs['odd'] if x % 2 != 0]

    if "even" in kwargs:
        kwargs['even'] = [int(x) for x in kwargs['even'] if x % 2 == 0]
     #   kwargs['even'] = filter(lambda  x: x % 2 == 0, kwargs['even'])  (tova e sustoto, no s filter)

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))  #x[1] защото така взимаме VALUE на речника


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
