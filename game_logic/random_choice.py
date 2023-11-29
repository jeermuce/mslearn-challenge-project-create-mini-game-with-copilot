def random_choice():
    import random
    value = random.randint(0, 2)
    if value == 0:
        print('Computer chose rock.')
    elif value == 1:
        print('Computer chose scissors.')
    elif value == 2:
        print('Computer chose paper.')
    return value
