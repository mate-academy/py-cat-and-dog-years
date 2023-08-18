from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,cat_age_as_human_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (100, 21)
    ],
    ids=[
        "cat age 0 must give 0 human age",
        "cat age in range (1, 15) give 0 human age",
        "cat age 15 years must give 1 human age",
        "cat age in range (15, 24) must give 1 human age",
        "cat age 25 must give 2 human age",
        "cat age in range (25, 28) must give 2 human age",
        "cat age equal 28 must give 3 human age",
        "if cats lived 100 years it will be 21 human age"
    ]
)
def test_cat_age_as_human_age(cat_age: int,
                              cat_age_as_human_age: int) -> None:
    assert get_human_age(cat_age, 0) == [cat_age_as_human_age, 0]


@pytest.mark.parametrize(
    "dog_age,dog_age_as_human_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (29, 3),
        (100, 17)
    ],
    ids=[
        "dog age 0 must give 0 human age",
        "dog age in range (1, 15) give 0 human age",
        "dog age 15 years must give 1 human age",
        "dog age in range (16, 24) give 1 human age",
        "dog age 24 must give 2 human age",
        "dog age in range (25, 29) must give 2 human age",
        "dog age 25 must give 3 human age",
        "if dogs lived 100 years it will be 17 human age"
    ]
)
def test_dog_age_as_human_age(dog_age: int,
                              dog_age_as_human_age: int) -> None:
    assert get_human_age(0, dog_age) == [0, dog_age_as_human_age]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param
        (
            "cat",
            "dog",
            TypeError,
            id="should raise error when parameter is not int"
        ),
    ]
)
def test_raising_errors_correctly(cat_age: int,
                                  dog_age: int,
                                  expected_error: Any) -> None:
    with pytest.raises(expected_error):
        assert get_human_age(cat_age, dog_age)
