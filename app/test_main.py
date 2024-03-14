import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="check if give zero age for cat and dog"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="check for cat and dog 14 years should return 0 human years"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="check for cat and dog 15 years should return 1 human years"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="check for cat and dog 23 years should return 1 human years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="check for cat and dog 24 years should return 2 human years"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="check for cat and dog 27 years should return 2 human years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="check for cat and dog 28 years should return "
               "3 human years for cat and 2 human years for dog"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="check for cat and dog 100 years should return "
               "21 human years for cat and 17 human years for dog"
        )
    ]

)
def test_get_human_age(cat_age: int, dog_age: int, expected_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age
