def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Cat and dog age must be an instance of int")

    human_cat = 0
    human_dog = 0

    if cat_age >= 15 and cat_age <= 24:
        human_cat = 1
        if cat_age == 24:
            human_cat = 2
    elif cat_age > 24:
        human_cat = 2 + ((cat_age - 24) // 4)

    if dog_age >= 15 and dog_age <= 24:
        human_dog = 1
        if dog_age == 24:
            human_dog = 2
    elif dog_age > 24:
        human_dog = 2 + ((dog_age - 24) // 5)

    return [human_cat, human_dog]
