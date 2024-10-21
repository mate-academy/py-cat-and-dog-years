import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            15,
            14,
            [1, 0],
            id="15 years animals is 1 human"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="27 years animals is 2 human"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dogs years is 3 human"
        ),
        pytest.param(
            100.1,
            100.5,
            [21, 17],
            id="remainder should be discarded"
        ),
        pytest.param(
            -5,
            -3,
            [0, 0],
            id="value is negative should return 0"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="value is 0 should return 0"
        ),
        pytest.param(
            1000,
            1000,
            [246, 197],
            id="result should be correct when value is large"
        ),
    ]
)
def test_modify_convert_to_human(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
