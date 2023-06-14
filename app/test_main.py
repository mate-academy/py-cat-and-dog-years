from app.main import get_human_age

# write your code here
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (15, 9, [1, 0]),
    (25, 15, [2, 1]),
    (32, 20, [3, 2]),
    (36, 22, [3, 2]),
    (40, 22, [4, 2]),
    (36, 24, [3, 3]),
    (45, 30, [5, 4]),
    (-5, 0, [0, 0]),
    (0, 0, [0, 0]),
    (1000000, 999999, [111112, 111111])
])
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
    # assert get_human_age(cat_age + 1, dog_age) != expected
    # assert get_human_age(cat_age, dog_age + 1) != expected


def test_get_human_age_fails_on_wrong_data():
    # Test incorrect data type
    with pytest.raises(TypeError):
        get_human_age("cat", 5)


@pytest.mark.parametrize("cat_age, dog_age", [
    (0, "0"),
    (0, [33]),
    (len, 0)
])
def test_get_human_age_raises_error(cat_age, dog_age):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
