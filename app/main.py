def get_human_age(cat_age: int, dog_age: int) -> list:

    def cat_age_to_human(age: int) -> int:

        if cat_age > 24:
            return ((cat_age - 24) // 4) + 2
        elif cat_age == 24:
            return 2
        else:
            return 0 if cat_age < 15 else 1

    def dog_age_to_human(age: int) -> int:

        if dog_age > 24:
            return ((dog_age - 24) // 5) + 2
        elif dog_age == 24:
            return 2
        else:
            return 0 if dog_age < 15 else 1

    return [cat_age_to_human(cat_age), dog_age_to_human(dog_age)]
