import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def test_should_return_elements(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_edge_case_negative_value() -> None:
    assert get_human_age(-1, -5) == [0, 0]


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", "15"),
    (None, 10),
    (10, None)
])
def test_called_error(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
