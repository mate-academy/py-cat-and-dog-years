import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            -1, -2, [0, 0],
            id="should return [0, 0] if values < 0"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should return [0, 0] if cat and dog age is 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return [0, 0] if cat and dog age is 14"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return [1, 1] if cat and dog age is 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return [1, 1] if cat and dog age is 23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return [2, 2] if cat and dog age is 24"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="should return [2, 2] if cat and dog age is 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should return [3, 2] if cat and dog age is 28"
        ),
        pytest.param(
            95, 95, [19, 16],
            id="should return [19, 16] if cat and dog age is 95"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
