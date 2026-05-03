def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def cat_convert(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1

        human = 2
        age -= 24

        while age >= 4:
            human += 1
            age -= 4

        return human

    def dog_convert(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1

        human = 2
        age -= 24

        while age > 5:
            human += 1
            age -= 5

        return human

    return [cat_convert(cat_age), dog_convert(dog_age)]
