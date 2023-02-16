import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        (0, 0, [0, 0]),
        (-27, 15, [0, 1]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_correct_result(cat: int, dog: int, result: list) -> None:
    assert (get_human_age(cat, dog) == result)


@pytest.mark.parametrize(
    "cat,dog",
    [
        ("dog", "cat"),
        ([], ()),
        (14, "12"),
    ]
)
def test_age_not_integer(cat: str, dog: str) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
