import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (10.5, 20.7, [0, 1]),
        (34.6, 34.6, [4, 4])
    ]
)
def test_with_correct_attributes(cat_age, dog_age, expected): # noqa
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("cat", "dog"),
        ([15], [20]),
        ({"cat": 17}, {"dog": 20}),
        ((5, ), (6, )),
        ({10}, {10})
    ]
)
def test_with_incorrect_attributes(cat_age, dog_age): # noqa
    with pytest.raises(TypeError):
        assert get_human_age(cat_age, dog_age)
