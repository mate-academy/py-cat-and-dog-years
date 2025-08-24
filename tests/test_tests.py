import pytest
from app.main import get_human_age

@pytest.mark.parametrize("cat, dog, expected", [
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_sample_cases(cat, dog, expected):
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize("cat, dog", [
    (-5, 30),
    (30, -5),
    ("cat", 30),
    (30, "dog"),
    (None, 0),
    (0, None),
    (3.14, 10),
    (10, 2.71),
])
def test_invalid_inputs(cat, dog):
    with pytest.raises(ValueError):
        get_human_age(cat, dog)
