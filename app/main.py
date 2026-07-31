def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError

    def convert_to_human(age: int, divisor: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // divisor

    return [
        convert_to_human(cat_age, 4),
        convert_to_human(dog_age, 5),
    ]
