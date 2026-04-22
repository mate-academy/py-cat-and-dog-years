def get_human_age(cat_age: int, dog_age: int) -> list:
    result = []

    if not isinstance(cat_age, int):
        raise TypeError

    elif cat_age < 0:
        raise ValueError

    elif cat_age < 15:
        result.append(0)
    elif cat_age < 24:
        result.append(1)
    elif cat_age < 28:
        result.append(2)
    elif cat_age == 28:
        result.append(3)
    else:
        cat_age -= 28
        age = 3
        age += cat_age // 4
        result.append(age)

    if not isinstance(dog_age, int):
        raise TypeError

    elif dog_age < 0:
        raise ValueError

    elif dog_age < 15:
        result.append(0)
    elif dog_age < 24:
        result.append(1)
    elif dog_age < 29:
        result.append(2)
    elif dog_age == 29:
        result.append(3)
    else:
        dog_age -= 29
        age = 3
        age += dog_age // 5
        result.append(age)

    return result
