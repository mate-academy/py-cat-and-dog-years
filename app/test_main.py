from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (-3, -5, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_animal(cat_age: int, dog_age: int, result: list) -> None:
    output = get_human_age(cat_age, dog_age)
    assert (output == result)
    assert isinstance(output, list)
    assert len(output) == 2
    assert all(isinstance(age, int) for age in output)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("0", 3),
        (4, None),
        ([0, 3], 2)
    ]
)
def test_invalid_types_raise_typeerror(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
