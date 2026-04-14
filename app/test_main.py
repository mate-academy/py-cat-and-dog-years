import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    # Below first threshold (< 15): 0 human years
    (0, 0, [0, 0]),
    (1, 1, [0, 0]),
    (14, 14, [0, 0]),

    # Exactly first threshold (15): 1 human year
    (15, 15, [1, 1]),

    # Between first and second threshold (15–23): still 1 human year
    (16, 16, [1, 1]),
    (23, 23, [1, 1]),

    # Exactly second threshold (24): 2 human years
    (24, 24, [2, 2]),

    # Cat gets extra year at 28, dog still at 2 (needs 29)
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),

    # Dog gets extra year at 29
    (29, 29, [3, 3]),

    # Cat extra years (every 4): 32 -> 4, 36 -> 5
    (32, 32, [4, 3]),
    (36, 36, [5, 4]),

    # Dog extra years (every 5): 34 -> 4, 39 -> 5
    (34, 34, [4, 4]),

    # Large values
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_returns_list():
    result = get_human_age(0, 0)
    assert isinstance(result, list)
    assert len(result) == 2


def test_cat_boundary_first_threshold():
    assert get_human_age(14, 0)[0] == 0
    assert get_human_age(15, 0)[0] == 1


def test_cat_boundary_second_threshold():
    assert get_human_age(23, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2


def test_cat_increments_every_4_years():
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(31, 0)[0] == 3
    assert get_human_age(32, 0)[0] == 4


def test_dog_boundary_first_threshold():
    assert get_human_age(0, 14)[1] == 0
    assert get_human_age(0, 15)[1] == 1


def test_dog_boundary_second_threshold():
    assert get_human_age(0, 23)[1] == 1
    assert get_human_age(0, 24)[1] == 2


def test_dog_increments_every_5_years():
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 33)[1] == 3
    assert get_human_age(0, 34)[1] == 4


def test_cat_and_dog_age_independently():
    # Cat at 28 = 3 human years, dog at 24 = 2 human years
    assert get_human_age(28, 24) == [3, 2]
    # Cat at 24 = 2 human years, dog at 29 = 3 human years
    assert get_human_age(24, 29) == [2, 3]
