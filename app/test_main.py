import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_age_in_human_age,dog_age_in_human_age",
    [
        (-10, -10, 0, 0),
        (7, 7, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ],
    ids=[
        "If cat/dog age is negative should return 0",
        "If cat/dog age is less than 15 should return 0",
        "If cat/dog age is 15 should return 1",
        "If cat/dog age is 23 should return 1",
        "If cat/dog age is 24 should return 2",
        "If cat/dog age is 27 should return 2",
        "If cat/dog age is 28 should return 3 for cat and 2 for dog",
        "Function is not working correctly with large numbers",
    ]
)
def test_correct_age_conversion(
    cat_age: int,
    dog_age: int,
    cat_age_in_human_age: int,
    dog_age_in_human_age: int
) -> None:
    assert (get_human_age(cat_age, dog_age)
            == [cat_age_in_human_age, dog_age_in_human_age])


@pytest.mark.parametrize(
    "cat_age,dog_age,error_type",
    [
        pytest.param("20", "20", TypeError)
    ]
)
def test_incorrect_data_type(
        cat_age: int,
        dog_age: int,
        error_type: Exception
) -> None:
    with pytest.raises(error_type):
        get_human_age(cat_age, dog_age)
