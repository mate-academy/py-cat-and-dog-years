from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,expected",
                         [(0, 0, [0, 0]),
                          (15, 15, [1, 1]),
                          (24, 24, [2, 2]),
                          (28, 28, [3, 2]),
                          (14, 14, [0, 0]),
                          (100, 100, [21, 17]),
                          (23, 23, [1, 1]),
                          (27, 27, [2, 2])])
def test_should_return_correct_human_age(cat_age: int,
                                         dog_age: int,
                                         expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_correct_exception() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", True)
    with pytest.raises(ValueError):
        get_human_age(-20, -30)
