import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero age gives zero human years",
        "14 years is still less than 1 human year",
        "15 years give 1 human year",
        "23 years still give 1 human year",
        "24 years give 2 human years",
        "27 cat and 28 dog years still give 2 human years",
        "28 cat and 29 dog years give 3 human years",
        "large ages are converted correctly",
    ]
)
def test_should_convert_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_negative_age_gives_zero_human_years() -> None:
    assert get_human_age(-1, -10) == [0, 0]


def test_should_raise_type_error_for_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
