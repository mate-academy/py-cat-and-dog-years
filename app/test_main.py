import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result_age",
    [
        (-5, -5, [0, 0]),
        (None, 5, TypeError),
        ("1", 5, TypeError),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])

    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       result_age: list[int]
                       ) -> None:
    if cat_age is None or dog_age is None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == result_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ("1", 1, TypeError),
        (2, None, TypeError),
    ]
)
def test_age_mast_to_be_type_int(cat_age: int,
                                 dog_age: int,
                                 error: type(TypeError)
                                 ) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
