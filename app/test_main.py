from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="Cat/Dog age less than 15 should be 0 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="Cat/Dog age should convert to one human year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="Cat/Dog age convert to second human year"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="Cat/Dog check third rule of converting"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Cat/Dog check longevity"
        )
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:

    assert get_human_age(cat_age, dog_age) == expected
