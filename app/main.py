def get_human_age(cat_age: int, dog_age: int) -> list:
    if (not isinstance(cat_age, (int, float))
            or not isinstance(dog_age, (int, float))):
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    def convert(age: int, step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // step

    cat_human = convert(cat_age, 4)
    dog_human = convert(dog_age, 5)

    return [int(cat_human), int(dog_human)]
