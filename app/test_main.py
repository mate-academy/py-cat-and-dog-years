import pytest

import app.main as main


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected  # <-- via módulo


def test_raises_on_wrong_type() -> None:
    with pytest.raises((TypeError, ValueError)):
        main.get_human_age("gato", "cão")
