def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert(age: int, step: int) -> int:
        if age < 15:
            return 0

        human_years = 1

        if age < 24:
            return human_years

        human_years += 1
        human_years += (age - 24) // step

        return human_years

    cat_human = convert(cat_age, 4)
    dog_human = convert(dog_age, 5)

    return [cat_human, dog_human]
