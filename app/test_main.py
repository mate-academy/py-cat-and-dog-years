import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_human_age", [
    pytest.param(-5, -4, [0, 0], id="test should gives 0 when entering negative numbers"),
    pytest.param(-9, 35, [0, 4], id="test should take negative age of cat and not affect age of dog"),
    pytest.param(35, -9, [4, 0], id="test should take negative age of dog and not affect age of cat"),
    pytest.param(0, 0, [0, 0], id="test should take age 0 and return 0"),
    pytest.param(15, 15, [1, 1], id="test should return 1 year when entering minimum animal age 15 dog/cat years old"),
    pytest.param(24, 24, [2, 2], id="test should return 2 year when entering minimum animal age 24 dog/cat years old"),
    pytest.param(28, 0, [3, 0], id="test should every 4 next cat years give 1 extra human year"),
    pytest.param(0, 29, [0, 3], id="test should every 5 next dog years give 1 extra human year")
])
def test_get_human_age(
        cat_age: int, dog_age: int,
        expected_human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
