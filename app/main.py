def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert_cat_age(age: int) -> int:
        if age <= 14:
            return 0
        elif age <= 23:
            return 1
        else:
            return 2 + (age - 24) // 4

    def convert_dog_age(age: int) -> int:
        if age <= 14:
            return 0
        elif age <= 23:
            return 1
        else:
            return 2 + (age - 24) // 5

    return [convert_cat_age(cat_age), convert_dog_age(dog_age)]
