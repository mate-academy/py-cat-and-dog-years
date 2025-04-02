import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_cat_age,expected_dog_age",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (23.1, 23.1, 1, 1),
        (23.9, 23.9, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (29, 29, 3, 3),
        (100, 100, 21, 17)
    ]
)
def test_cat_and_dog_age_convertion_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_cat_age: int,
        expected_dog_age: int
) -> None:
    assert (get_human_age(cat_age, dog_age)
            == [expected_cat_age, expected_dog_age])


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_exception",
    [
        (-1, 0, ValueError),
        (0, -1, ValueError),
        ("0", 0, TypeError),
        (0, "0", TypeError),
    ]
)
def test_if_raise_errors(cat_age: int,
                         dog_age: int,
                         expected_exception: type[BaseException]
                         ) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
