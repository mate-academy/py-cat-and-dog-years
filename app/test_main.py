import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,exception", [
    (-10, 12, ValueError),
    (10, -12, ValueError),
    (101, 34, ValueError),
    (34, 111, ValueError),
    ([1, 2], 34, TypeError),
    (34, [12], TypeError),
    ("0", 5, TypeError),
    (0, "0", TypeError)
])
def test_func_should_raise_correct_exception(
        cat_age: int,
        dog_age: int,
        exception: Exception
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,dog_age", [
    (17, 19),
    (55, 45),
    (12, 11)
])
def test_func_always_should_return_list_of_two_int(
        cat_age: int,
        dog_age: int
) -> None:
    value = get_human_age(cat_age, dog_age)
    assert isinstance(value, list) and len(value) == 2
    assert isinstance(value[0], int) and isinstance(value[1], int)


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (14, 0, [0, 0]),
    (0, 14, [0, 0]),
    (15, 15, [1, 1]),
    (16, 15, [1, 1]),
    (15, 16, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (15, 24, [1, 2]),
    (24, 15, [2, 1]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (27, 29, [2, 3]),
    (32, 29, [4, 3]),
    (55, 53, [9, 7]),
    (56, 54, [10, 8]),
    (100, 100, [21, 17])
])
def test_func_always_should_return_correct_result(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
