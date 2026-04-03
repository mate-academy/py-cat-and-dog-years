def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be int")

    def cat(age: int) -> int:
        if age < 0:
            return 0
        if age < 15:
            return 0
        if age < 24:
            return 1
        if age < 28:
            return 2
        return (age - 28) // 4 + 3

    def dog(age: int) -> int:
        if age < 0:
            return 0
        if age < 15:
            return 0
        if age < 24:
            return 1
        if age < 28:
            return 2
        return (age - 24) // 5 + 2

    return [cat(cat_age), dog(dog_age)]
