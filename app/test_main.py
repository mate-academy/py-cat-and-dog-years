import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected_result"),
    [
        (14, 14, [0, 0]),
        (15, 14, [1, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 23, [2, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        pytest.param(1000, 1500, [246, 297],
                     id="Function should handle big numbers"),
        pytest.param(0, 0, [0, 0],
                     id="When cat/dog years is 0 the result should be [0, 0]"),
        pytest.param(-15, -15, [0, 0],
                     id="For negative value the result should be [0 ,0]"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list[int]
                       ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
