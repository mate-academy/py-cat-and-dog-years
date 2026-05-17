def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def _convert_age(
        age: int,
        first_threshold: int,
        second_threshold: int,
        extra_rate: int,
    ) -> int:
        if age < first_threshold:
            return 0

        human_years = 1
        remaining = age - first_threshold

        if remaining < second_threshold:
            return human_years

        human_years += 1
        remaining -= second_threshold
        human_years += remaining // extra_rate
        return human_years

    cat_human_age = _convert_age(
        cat_age,
        first_threshold=15,
        second_threshold=9,
        extra_rate=4,
    )
    dog_human_age = _convert_age(
        dog_age,
        first_threshold=15,
        second_threshold=9,
        extra_rate=5,
    )
    return [cat_human_age, dog_human_age]
