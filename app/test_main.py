import pytest
from app.main import get_human_age

# write your code here
@pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
        ]
)
def test_human_age(cat_age: int,
                   dog_age: int,
                   expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (1000, 1000, [244, 198]),
            (10000, 10000, [2484, 1998]),
        ]
)
def test_get_human_age_large_numbers(cat_age: int,
                                     dog_age: int,
                                     expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_get_human_age_invalid_input():
    with pytest.raises(ValueError):
        get_human_age(-1, 10)
    with pytest.raises(ValueError):
        get_human_age(10, -1)
    with pytest.raises(TypeError):
        get_human_age("10", 10)
    with pytest.raises(TypeError):
        get_human_age(10, "10")
    with pytest.raises(TypeError):
        get_human_age(10.5, 10)
    with pytest.raises(TypeError):
        get_human_age(10, 10.5)
