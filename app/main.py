def get_human_age(cat_age: int, dog_age: int) -> list:

    def convert_age(age: int, step: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // step

    return [
        convert_age(cat_age, 4),
        convert_age(dog_age, 5)
    ]
