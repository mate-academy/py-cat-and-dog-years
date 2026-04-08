def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    def calculate(age: int, step: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // step

    return [calculate(cat_age, 4), calculate(dog_age, 5)]
