import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(32, 29, [4, 3]),
        pytest.param(28, 34, [3, 4]),
        pytest.param(-10, -10, [0, 0]),
        pytest.param(1000000, 1000000, [249996, 199997])
    ],
    ids=[
        "Dog/cat age 0 should return 0",
        "Dog/cat under 15 years should give 0 human year.",
        "First 15-23 dog/cat years should give 1 human year.",
        "Next 9(24+) dog/cat years should give 1 more human year.",
        "Every next 4 cat years should give 1 more human year.",
        "Every next 5 dog years should give 1 more human year.",
        "Negative dog/cat age should give 0 human age.",
        "Really big numbers should work correctly."
    ]
)
def test_cat_dog_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        (10, "30", TypeError),
        (None, 20, TypeError)
    ],
    ids=[
        "'str' cannot be a function parameter.",
        "'None' cannot be a function parameter."
    ]
)
def test_invalid_type(
        cat_age: int,
        dog_age: int,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
