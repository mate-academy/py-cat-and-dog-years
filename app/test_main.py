from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age, expected", [
                        (0, 0, [0, 0]),
                        (14, 14, [0, 0]),
                        (15, 15, [1, 1]),
                        (28, 28, [3, 2]),
                        (100, 100, [21, 17]),
                        (24, 15, [2, 1]),
                        (23, 23, [1, 1]),
                        (24, 24, [2, 2]),
                        (-1, 0, [0, 0]),
                        (200, 200, [46, 37])
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_srt_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", 0)
