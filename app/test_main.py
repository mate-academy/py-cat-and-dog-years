import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (1, 1, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (16, 16, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (32, 32, [4, 3]),
    (33, 33, [4, 3]),
    (34, 34, [4, 4]),
    (100, 100, [21, 17]),
    (-1, -1, [0, 0]),
])
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_returns_list() -> None:
    result = get_human_age(15, 15)
    assert isinstance(result, list)
    assert len(result) == 2


def test_string_input_raises_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
