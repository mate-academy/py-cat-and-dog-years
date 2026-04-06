def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert_age_to_human(age: int, divisor: int) -> int:
        if not isinstance(age, int):
            raise TypeError
        if age < 0:
            raise ValueError
        if age < 15:
            return 0
        elif age < 24:
            return 1
        return 2 + (age - 24) // divisor

    convert_age_cat_to_human = convert_age_to_human(cat_age, 4)
    convert_age_dog_to_human = convert_age_to_human(dog_age, 5)
    return [convert_age_cat_to_human, convert_age_dog_to_human]
