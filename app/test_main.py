import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),  # both ages are zero
        (14, 14, [0, 0]),  # before first human year
        (28, 28, [3, 2]),  # cat age increases, dog stays the same
        (100, 100, [21, 17]),  # large nums
    ],
    ids=[
        "zero_cat_and_dog_age",
        "before_first_human_year",
        "cat_ages_faster_than_dog",
        "large_ages",
    ]
)
def test_get_human_age_valid_cases(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),  # negative cat age
        (5, -1),  # negative dog age
        ("cat", 5),  # non-integer cat age
        (5, "dog"),  # non-integer dog age
        (None, 5),  # None as cat age
        (5, None),  # None as dog age
    ],
    ids=[
        "negative_cat_age",
        "negative_dog_age",
        "non_integer_cat_age",
        "non_integer_dog_age",
        "none_cat_age",
        "none_dog_age",
    ]
)
def test_get_human_age_invalid_cases(cat_age, dog_age) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list) and len(result) == 2
    except Exception as e:
        assert isinstance(e, (ValueError, TypeError))
