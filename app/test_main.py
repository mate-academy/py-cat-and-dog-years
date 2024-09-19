import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="should convert 14/14 into 0 human age"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should convert 15/15 into 1 human age"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should convert 23/23 into 1 human age"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should convert 24/24 into 2 human age"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="should convert 27/28 into 2 human age"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should convert 28/29 into 3 human age"
        )
    ]
)
def test_get_human_age(cat_age, dog_age, expected_result) -> None:
    list_of_ages = get_human_age(cat_age, dog_age)
    assert list_of_ages == expected_result
