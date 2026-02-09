def convert_cat_age(
        cat_age: int,
        first_span: int = 15,
        second_span: int = 9,
        next_span_leng: int = 4
) -> int:
    if not isinstance(cat_age, int):
        raise TypeError("Age must be an integer")
    human = 0
    if cat_age < 0:
        return 0
    if cat_age >= first_span:
        human += 1
        cat_age -= first_span
    else:
        return 0
    if cat_age >= second_span:
        human += 1
        cat_age -= second_span
    else:
        return human
    human += cat_age // next_span_leng
    return human


def convert_dog_age(
        dog_age: int,
        first_span: int = 15,
        second_span: int = 9,
        next_span_leng: int = 5
) -> int:
    if not isinstance(dog_age, int):
        raise TypeError("Age must be an integer")
    human2 = 0
    if dog_age < 0:
        return 0
    if dog_age >= first_span:
        human2 += 1
        dog_age -= first_span
    else:
        return 0
    if dog_age >= second_span:
        human2 += 1
        dog_age -= second_span
    else:
        return human2
    human2 += dog_age // next_span_leng
    return human2


def get_human_age(
        cat_age: int,
        dog_age: int
) -> list[int]:
    cat_human = convert_cat_age(
        cat_age,
        # first_span=15,
        # second_span=9,
        # next_span_leng=4
    )
    dog_human = convert_dog_age(
        dog_age,
        # first_span=15,
        # second_span=9,
        # next_span_leng=5
    )

    return [cat_human, dog_human]
