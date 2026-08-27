def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    def convert_to_human(age: int, step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        if age >= 24:
            return 2 + (age - 24) // step
    cat_human_age = convert_to_human(cat_age, 4)
    dog_human_age = convert_to_human(dog_age, 5)
    return [cat_human_age, dog_human_age]
