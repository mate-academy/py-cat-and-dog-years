import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-15, -30, [0, 0])
    ]
)
def test_for_correct_working_func(cat_age: int,
                                  dog_age: int,
                                  expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        ("15", 0, TypeError),
        (0, "15", TypeError)
    ]
)
def test_incorrect_type_age(cat_age: int,
                            dog_age: int,
                            expected: BaseException) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)


def test_when_dog_age_is_negative() -> None:
    assert get_human_age(15, -15) == [1, 0]


def test_when_cat_age_is_negative() -> None:
    assert get_human_age(-15, 15) == [0, 1]
