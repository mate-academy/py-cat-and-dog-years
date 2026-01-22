import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_age_calculated_correctly(cat_age: int,
                                  dog_age: int,
                                  human_age: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    ), f"Cat age {cat_age} and dog age {dog_age} should"\
        f"be human age {human_age} respectively."


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (1, 0),
        (14, 2),
        (111, 15),
        (24, 120)]
)
def test_age_is_realistic(cat_age: int, dog_age: int) -> None:
    assert (
        0 <= cat_age <= 120 and 0 <= dog_age <= 120
    ), f"Cat age {cat_age} and dog age {dog_age} should be between 0 and 120."
    print(cat_age, dog_age)


def test_years_are_digits() -> None:
    with pytest.raises(TypeError):
        get_human_age("0", "0")
