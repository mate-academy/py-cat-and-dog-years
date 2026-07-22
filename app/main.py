def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, extra_bracket_step: int) -> int:
        human_years = 0
        remaining = age

        first_stage = min(remaining, 15)
        remaining -= first_stage
        if first_stage == 15:
            human_years += 1

        if remaining <= 0:
            return human_years

        second_stage = min(remaining, 9)
        remaining -= second_stage
        if second_stage == 9:
            human_years += 1

        if remaining <= 0:
            return human_years

        human_years += remaining // extra_bracket_step
        return human_years

    cat_human_age = convert(cat_age, 4)
    dog_human_age = convert(dog_age, 5)
    return [cat_human_age, dog_human_age]
