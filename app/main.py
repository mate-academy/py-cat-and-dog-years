def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    human_cat = (cat_age >= 15) + (cat_age >= 24)
    if cat_age >= 24:
        human_cat += (cat_age - 24) // 4

    human_dog = (dog_age >= 15) + (dog_age >= 24)
    if dog_age >= 24:
        human_dog += (dog_age - 24) // 5

    return [human_cat, human_dog]
