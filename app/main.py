def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 15:
        cat_human = 0
    elif cat_age < 24:
        cat_human = 1
    else:
        cat_human = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        dog_human = 0
    elif dog_age < 24:
        dog_human = 1
    else:
        dog_human = 2 + (dog_age - 24) // 5

    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Возраст должен быть целым числом")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Возраст не может быть отрицательным")

    return [cat_human, dog_human]
