import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result", [
        pytest.param(
            0, 0, [0, 0],
            id="zero values"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="first year border"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="achieving first year border"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="second year border"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="achieving second year border"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="cat's third year border"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="difference between animals"
        ),
        pytest.param(
            200, 200, [46, 37],
            id="big numbers"
        ),
        pytest.param(
            -5, -5, [0, 0],
            id="negative numbers"
        ),
        pytest.param(
            -10, 20, [0, 2],
            id="negative cat age with positive dog age"
        ),
        pytest.param(
            10, -20, [0, 1],
            id="positive cat age with negative dog age"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age should be an integer.")
    assert get_human_age(cat_age, dog_age) == result
