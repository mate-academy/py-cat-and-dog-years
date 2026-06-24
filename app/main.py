def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, step: int) -> int:
        if age <= 14:
            return 0
        years = 1
        age -= 15
        if age < 9:
            return years
        years += 1
        age -= 9
        years += age // step
        return round(years, 1)

    return [convert(cat_age, 4), convert(dog_age, 5)]
