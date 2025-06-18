from app.main import get_human_age
import pytest

@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_convert_into_human_age_correctly(a: int,
                                          b: int,
                                          result: list[int]
                                          ) -> None:
    assert get_human_age(a, b) == result
