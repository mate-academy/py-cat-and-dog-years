def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, step: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // step

    return [convert(cat_age, 4), convert(dog_age, 5)]
