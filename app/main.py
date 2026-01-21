def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    cat_age = max(0, cat_age)
    dog_age = max(0, dog_age)

    def cat_to_human(age: int) -> int:
        human = 0
        if age >= 15:
            human += 1
        if age >= 24:
            human += 1
        if age > 27:
            human += (age - 28) // 4 + 1
        return human

    def dog_to_human(age: int) -> int:
        human = 0
        if age >= 15:
            human += 1
        if age >= 24:
            human += 1
        if age > 28:
            human += (age - 29) // 5 + 1
        return human

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
