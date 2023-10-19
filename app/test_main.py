from app.main import get_human_age


def test_human_age_by_cat_and_dog_age() -> None:
    dog_age, cat_age = 0, 0
    result = get_human_age(dog_age, cat_age)
    expected = [0, 0]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 14, 14
    result = get_human_age(dog_age, cat_age)
    expected = [0, 0]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 15, 15
    result = get_human_age(dog_age, cat_age)
    expected = [1, 1]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 23, 23
    result = get_human_age(dog_age, cat_age)
    expected = [1, 1]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 24, 24
    result = get_human_age(dog_age, cat_age)
    expected = [2, 2]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 27, 27
    result = get_human_age(dog_age, cat_age)
    expected = [2, 2]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 28, 28
    result = get_human_age(dog_age, cat_age)
    expected = [3, 2]

    assert result == expected, f"should convert into {result} human age"

    dog_age, cat_age = 100, 100
    result = get_human_age(dog_age, cat_age)
    expected = [21, 17]

    assert result == expected, f"should convert into {result} human age"
