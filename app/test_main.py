from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        ("cat", "dog", pytest.raises(TypeError)),
        (1.5, 2.5, pytest.raises(TypeError)),
        (True, False, pytest.raises(TypeError)),
        ([15], [9], pytest.raises(TypeError)),
        ({"age": 15}, {"age": 9}, pytest.raises(TypeError))

    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    if isinstance(result, list):
        assert get_human_age(cat_age, dog_age) == result
    elif isinstance(result, type) and issubclass(result, Exception):
        with pytest.raises(result):
            get_human_age(cat_age, dog_age)
