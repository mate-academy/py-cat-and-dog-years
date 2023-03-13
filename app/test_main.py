import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, result",
                         [
                             (0, 0, [0, 0]),
                             (14, 14, [0, 0]),
                             (15, 15, [1, 1]),
                             (23, 23, [1, 1]),
                             (24, 24, [2, 2]),
                             (27, 27, [2, 2]),
                             (28, 28, [3, 2]),
                             (100, 100, [21, 17])
                         ],
                         ids=[
                             "check cat and dog zero years",
                             "check cat and dog zero years",
                             "check cat and dog one years",
                             "check cat and dog one years",
                             "check cat and dog two years",
                             "check cat and dog two years",
                             "check cat and dog more than two years",
                             "check cat and dog more than two years",
                         ])
def test_cat_and_dog_years(cat_age: int,
                           dog_age: int,
                           result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize("cat_age, dog_age, error",
                         [
                             ("30", 30, TypeError),
                             (30, [30], TypeError),
                             ("30", "30", TypeError)
                         ],
                         ids=[
                             "raise exception when receive incorrect type",
                             "raise exception when receive incorrect type",
                             "raise exception when receive incorrect type",
                         ])
def test_raising_errors_correctly(cat_age: int,
                                  dog_age: int,
                                  error: Exception) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
