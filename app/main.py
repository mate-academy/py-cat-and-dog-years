def get_human_age(cat_age: int, dog_age: int) -> list:

    if cat_age < 0 or dog_age < 0 or cat_age > 100 or dog_age > 100:
        raise ValueError
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    def calculate(age: int, step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // step

    return [calculate(cat_age, 4), calculate(dog_age, 5)]
