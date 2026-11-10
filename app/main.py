def get_human_age(cat_age: int, dog_age: int) -> list:
    if type(cat_age) is not int and type(dog_age) is not int:
        raise TypeError("Ages must be integers")

    human_cat = 0
    human_dog = 0

    if cat_age >= 15:
        human_cat += 1
        if cat_age >= 24:
            human_cat += 1
            human_cat += (cat_age - 24) // 4

    if dog_age >= 15:
        human_dog += 1
        if dog_age >= 24:
            human_dog += 1
            human_dog += (dog_age - 24) // 5

    return [human_cat, human_dog]
