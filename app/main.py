def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError()

    if cat_age < 0 or dog_age < 0:
        raise ValueError()
    cat_human_age = 0
    dog_human_age = 0

    for i in range(cat_age + 1):
        if i == 15:
            cat_human_age = 1
        if i == 24:
            cat_human_age = 2
        if i > 24 and i % 4 == 0:
            cat_human_age = cat_human_age + 1

    for i in range(dog_age + 1):
        if i == 15:
            dog_human_age = 1
        if i == 24:
            dog_human_age = 2
        if i > 24 and (i - 24) % 5 == 0:
            dog_human_age = dog_human_age + 1

    return [cat_human_age, dog_human_age]
