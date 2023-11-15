from app.main import get_human_age


def test_human_age_should_be_equal_to_0() -> None:
    cat_age = 14
    dog_age = 14
    result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        dog_age < 15 and cat_age < 15 and result == [0, 0]
    ), (
        f"For cat age {cat_age} and {dog_age}, "
        f"expected result is [0, 0], but got {result}"
    )


def test_human_age_should_be_equal_to_1() -> None:
    cat_age = 23
    dog_age = 23
    result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        dog_age < 24 and cat_age < 24 and result == [1, 1]
    ), (
        f"For {cat_age} and {dog_age}, "
        f"expected result is [1, 1], but got {result}"
    )


def test_human_age_should_be_equal_to_2() -> None:
    cat_age = 27
    dog_age = 28
    result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        dog_age < 29 and cat_age < 28 and result == [2, 2]
    ), (
        f"For {cat_age} and {dog_age}, "
        f"expected result is [2, 2], but got {result}"
    )


def test_human_age_should_be_more_than_2() -> None:
    cat_age = 100
    dog_age = 100
    result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        result == [21, 17]
    ), (
        f"For {cat_age} and {dog_age}, "
        f"expected result is [2, 2], but got {result}"
    )
