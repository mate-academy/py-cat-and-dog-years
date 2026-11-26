def get_human_age(cat_age: int, dog_age: int) -> list:

    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    cat_human_age = 0
    if 15 <= cat_age <= 23:
        cat_human_age = 1
    elif cat_age > 23:
        cat_human_age = (cat_age - 24) // 4 + 2

    dog_human_age = 0
    if 15 <= dog_age <= 23:
        dog_human_age = 1
    elif dog_age > 23:
        dog_human_age = (dog_age - 24) // 5 + 2

    return [cat_human_age, dog_human_age]
