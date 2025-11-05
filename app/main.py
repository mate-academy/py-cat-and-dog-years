def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert_cat(age: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 4

    def convert_dog(age: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 5

    return [convert_cat(cat_age), convert_dog(dog_age)]
