import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (-1, -3, [0, 0])
])
def test_get_human_age(cat_age: int, dog_age: int,
                       expected_result: list[int]) -> None:
    result = get_human_age(cat_age, dog_age)
    assert expected_result == result


@pytest.mark.parametrize("cat_age, dog_age, expected_exception", [
    ("1", "2", TypeError),
    ([1], [2], TypeError),
    ({1}, {2}, TypeError),
    (1.2, 2.3, TypeError),
    (True, True, TypeError)

])
def test_get_human_age_on_exceptions(cat_age: int, dog_age: int,
                                     expected_exception: Exception) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
