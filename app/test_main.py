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
    (36, 36, [5, 4]),
    (34, 34, [4, 4]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_returns_list() -> None:
    result = get_human_age(0, 0)
    assert isinstance(result, list)
    assert len(result) == 2


def test_cat_boundary_first_threshold() -> None:
    assert get_human_age(14, 0)[0] == 0
    assert get_human_age(15, 0)[0] == 1


def test_cat_boundary_second_threshold() -> None:
    assert get_human_age(23, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2


def test_cat_increments_every_4_years() -> None:
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(31, 0)[0] == 3
    assert get_human_age(32, 0)[0] == 4


def test_dog_boundary_first_threshold() -> None:
    assert get_human_age(0, 14)[1] == 0
    assert get_human_age(0, 15)[1] == 1


def test_dog_boundary_second_threshold() -> None:
    assert get_human_age(0, 23)[1] == 1
    assert get_human_age(0, 24)[1] == 2


def test_dog_increments_every_5_years() -> None:
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 33)[1] == 3
    assert get_human_age(0, 34)[1] == 4


def test_cat_and_dog_age_independently() -> None:
    assert get_human_age(28, 24) == [3, 2]
    assert get_human_age(24, 29) == [2, 3]
