import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (
            0,
            0,
            [0, 0]
        ),
        (
            14,
            14,
            [0, 0]
        ),
        (
            15,
            15,
            [1, 1]
        ),
        (
            23,
            23,
            [1, 1]
        ),
        (
            24,
            24,
            [2, 2]
        ),
        (
            27,
            27,
            [2, 2]
        ),
        (
            28,
            28,
            [3, 2]
        ),
        (
            100,
            100,
            [21, 17]
        ),
        (
            -5,
            -5,
            [0, 0]
        ),
    ]
)
def test_should_return_15_years_for_1_human_year(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_cannot_recieve_non_int_values() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", "2")
