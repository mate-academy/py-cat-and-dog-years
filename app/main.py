def get_human_age(cat_age: int, dog_age: int) -> list:

    for age in (cat_age, dog_age):
        if isinstance(age, bool) or not isinstance(age, int):
            raise TypeError
        if age < 0:
            raise ValueError

    def cat_to_human(age: int) -> int:
        human = 0
        if age >= 15:
            human += 1
            age -= 15
        else:
            return 0
        if age >= 9:
            human += 1
            age -= 9
        else:
            return human
        human += age // 4
        return human

    def dog_to_human(age: int) -> int:
        human = 0
        if age >= 15:
            human += 1
            age -= 15
        else:
            return 0
        if age >= 9:
            human += 1
            age -= 9
        else:
            return human
        human += age // 5
        return human

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
