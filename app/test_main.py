import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, "
                         "dog_age, "
                         "result",
                         [(0, 0, [0, 0]),
                          (14, 14, [0, 0])])
def test_cat_and_dog_zero_years(cat_age: int,
                                dog_age: int,
                                result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize("cat_age,"
                         "dog_age, "
                         "result",
                         [(15, 15, [1, 1]),
                          (23, 23, [1, 1])])
def test_cat_and_dog_one_years(cat_age: int,
                               dog_age: int,
                               result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize("cat_age, "
                         "dog_age, "
                         "result",
                         [(24, 24, [2, 2]),
                          (27, 27, [2, 2])])
def test_cat_and_dog_two_years(cat_age: int,
                               dog_age: int,
                               result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize("cat_age, "
                         "dog_age, "
                         "result",
                         [(28, 28, [3, 2]),
                          (100, 100, [21, 17])])
def test_cat_and_dog_more_than_two_years(cat_age: int,
                                         dog_age: int,
                                         result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
