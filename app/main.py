def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert_age(age: int,
                    first: int,
                    second: int,
                    step: int) -> int:
        human_years = 0
        if age <= first:
            human_years += age
            return human_years
        human_years += first
        age -= first
        if age <= second:
            human_years += 1
            return human_years
        human_years += 1
        age -= second
        human_years += age // step
        return human_years

    cat_human = convert_age(cat_age, first=15, second=9, step=4)
    dog_human = convert_age(dog_age, first=15, second=9, step=5)
    return [cat_human, dog_human]
