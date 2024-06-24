import pytest
from  app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected", [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
        (-1, -1, [0, 0]),
         ([10,10],10, pytest.raises(TypeError)),
        ([{10:10}],10, pytest.raises(TypeError)),
        ("10", 10, pytest.raises(TypeError))]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: get_human_age
) -> None:
    if isinstance(expected, list):
        assert get_human_age(cat_age, dog_age) == expected
    else:
        with expected:
            get_human_age(cat_age, dog_age)