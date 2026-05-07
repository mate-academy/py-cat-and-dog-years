def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, second_threshold: int, step: int) -> int:
        if age < 15:
            return 0
        human = 1
        age -= 15
        if age >= second_threshold:
            human += 1
            age -= second_threshold
            human += age // step
        return human

    return [convert(cat_age, 9, 4), convert(dog_age, 9, 5)]
