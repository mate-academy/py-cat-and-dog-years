def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, step: int) -> int:
        if age < 15:
            return 0
        age -= 15
        if age == 0:
            return 1
        if age < 9:
            return 1
        if age == 9:
            return 2
        age -= 9
        return 2 + age // step
    return [convert(cat_age, 4), convert(dog_age, 5)]
