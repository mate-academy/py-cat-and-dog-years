def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError()
    if cat_age < 0 or dog_age < 0:
        raise ValueError()
    ls = []
    if cat_age < 15 :
        ls.append(0)
    elif cat_age < 24:
        ls.append(1)
    else:
        ls.append(2 + (cat_age - 24) // 4)

    if dog_age < 15:
        ls.append(0)
    elif dog_age < 24:
        ls.append(1)
    else:
        ls.append(2 + (dog_age - 24) // 5)
    return ls
