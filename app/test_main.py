import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_value",
    [
        pytest.param(
            0, 0,
            [0, 0],
            id="should return zero when dog-cat ages equal 0"
        ),
        pytest.param(
            14, 14,
            [0, 0],
            id="should return zero when dog-cat ages less 14"
        ),
        pytest.param(
            15, 15,
            [1, 1],
            id="15 dog-cat years equal 1 human years"
        ),
        pytest.param(
            23, 23,
            [1, 1],
            id="23 cat-gog year not enough for 2 human years"
        ),
        pytest.param(
            24, 24,
            [2, 2],
            id="24 dog-cat years equals 2 human years"
        ),
        pytest.param(
            27, 27,
            [2, 2],
            id="27 dog-cat years not enough for 3 human years"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="28 cat years is equal 3 human years"
        ),
        pytest.param(
            100, 100,
            [21, 17],
            id="100 cat years equal 21 human years,"
               "100 dog years equal 17 human years"
        )
    ]
)
def test_dog_cat_ages_equal_human_age(
        cat_age: int,
        dog_age: int,
        expected_value: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_value
