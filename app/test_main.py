import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (26, 26, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_calculate_years(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (
        f"Error cat age {cat_age} and dog age {dog_age}. "
        f"Expexted {result}"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 17),
        (19, [25]),
    ]
)
def test_cannot_pass_if_arent_integers(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-3, -5),
        (100000000000, 300000000000),
        (0, 0),
    ]
)
def test_negative_zeros_or_huge_numbers(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
