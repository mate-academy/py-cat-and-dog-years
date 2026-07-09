def get_human_age(cat_age: int, dog_age: int) -> list:
    def count_age(age_raw: int, step: int) -> int:
        if not isinstance(age_raw, (int, float)):
            raise TypeError
        age = int(age_raw)
        if age <= 14:
            return 0
        elif age in range(15, 24):
            return 1
        else:
            return (age - 24) // step + 2

    return [count_age(cat_age, 4), count_age(dog_age, 5)]
