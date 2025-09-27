from app.main import get_human_age

import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age_examples(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_edge_cases() -> None:
    assert get_human_age(15, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(32, 0)[0] == 4


def test_dog_edge_cases() -> None:
    assert get_human_age(0, 15)[1] == 1
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 34)[1] == 4
