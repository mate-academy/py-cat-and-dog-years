def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age, factor):
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // factor

    return [convert(cat_age, 4), convert(dog_age, 5)]
