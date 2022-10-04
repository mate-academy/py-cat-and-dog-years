import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            -1, -1, [0, 0],
            id="Return [0, 0] if animals ages are negative"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="Return [0, 0] if animals ages are equal 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Return [0, 0] if animals ages are less than 15"
        ),
        pytest.param(
            15, 23, [1, 1],
            id="Return [1, 1] if animals ages are between 15 and 23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Return [2,2] if animals ages are greater than 23"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Return [3, 2] if animals ages are 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Should return [100, 100] if animals ages are 100"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
