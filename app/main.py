def get_human_age(cat_age: int, dog_age: int) -> list:
    def to_human(age: int, third_step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // third_step

    return [to_human(cat_age, 4), to_human(dog_age, 5)]
