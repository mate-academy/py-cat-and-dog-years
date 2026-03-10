def convert(age: int, later_span: int) -> int:
    if age < 0:
        return 0
    if age < 15:
        return 0

    human = 1
    remaining = age - 15

    if remaining >= 9:
        human += 1
        remaining -= 9
    else:
        return human

    if remaining > 0:
        human += remaining // later_span

    return human


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    return [convert(cat_age, 4), convert(dog_age, 5)]
