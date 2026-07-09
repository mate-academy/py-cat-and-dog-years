def get_human_age(cat_age: int, dog_age: int) -> list:
    def count_age(age_raw: int, step: int) -> int:
        age = int(age_raw)
        if age <= 14:
            return 0
        elif age in range(15, 25):
            return 1
        elif age in range(25, 30):
            return 2
        else:
            return (age - 30) // step + 2

    return [count_age(cat_age, 4), count_age(dog_age, 5)]
