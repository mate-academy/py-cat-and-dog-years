import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age ,dog_age, expected_age",
    [
        pytest.param(
            28,
            28,
            [3, 2],
            id="output should not be changed"
        ),
        pytest.param(
            -20,
            0,
            [0, 0],
            id="should return zeros when passed negative or zero"
        )
    ]
)
def test_human_age(
        cat_age: int,
        dog_age: int,
        expected_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age
