import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Should return [0, 0] when cat and dog ages are equal 0"
        ),
        pytest.param(
            -10, -10, [0, 0],
            id="Should return [0, 0] when ages are negative"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Should return [0, 0] when cat and dog ages are less then 15"
        ),
        pytest.param(
            15, 23, [1, 1],
            id="Should return [1, 1] when animal age between 15 and 23"
        ),
        pytest.param(
            25, 25, [2, 2],
            id="Should return [2,2] when cat and dog ages are 25"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Should return [3, 2] when cat and dog ages are 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Should return [100, 100] when cat and dog ages are 100"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
