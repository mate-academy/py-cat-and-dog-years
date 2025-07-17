def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int):
        raise TypeError(f"cat_age must be an integer, got "
                        f"{type(cat_age).__name__}.")
    if not isinstance(dog_age, int):
        raise TypeError(f"dog_age must be an integer, got "
                        f"{type(dog_age).__name__}.")

    if cat_age < 0:
        raise ValueError(f"cat_age cannot be negative: received {cat_age}.")
    if dog_age < 0:
        raise ValueError(f"dog_age cannot be negative: received {dog_age}.")

    def cat_to_human(years: int) -> int:
        if years < 15:
            return 0
        years -= 15
        human_years = 1

        if years >= 9:
            years -= 9
            human_years += 1
        else:
            return human_years

        human_years += years // 4
        return human_years

    def dog_to_human(years: int) -> int:
        if years < 15:
            return 0
        years -= 15
        human_years = 1

        if years < 9:
            return human_years
        years -= 9
        human_years += 1

        human_years += years // 5
        return human_years

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
