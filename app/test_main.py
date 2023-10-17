import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age_of_cat_and_dog",
    [
        pytest.param(0, 0, [0, 0],
                     id="test should return zeroes if parameters zeroes"),
        pytest.param(14, 14, [0, 0],
                     id="test should return zeroes if "
                        "parameters are less than first year"),
        pytest.param(15, 15, [1, 1],
                     id="test should return [1, 1] if parameters "
                        "are less than sum 2 years"),
        pytest.param(23, 23, [1, 1],
                     id="test should round down results"),
        pytest.param(28, 28, [3, 2],
                     id="test may return different results "
                        "for different animals"),
        pytest.param(100, 100, [21, 17],
                     id="test should work with big numbers")
    ]
)
def test_correct_human_age(
        cat_age: int,
        dog_age: int,
        human_age_of_cat_and_dog: int
) -> None:
    assert (get_human_age(cat_age, dog_age) == human_age_of_cat_and_dog), \
        (f"Human age of {cat_age} cats years and {dog_age} dogs years "
         f"should be equal to {human_age_of_cat_and_dog}")
