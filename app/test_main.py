from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2])
    ]
)
def test_different_data(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result


def test_raise_error(cat: int, dog: int, result: list) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
