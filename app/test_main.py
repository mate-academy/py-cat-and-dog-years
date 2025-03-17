import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_res",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (10000, 10000, [2496, 1997])
    ]
)
def test_animals_age_convert_to_human_age(cat_age: int,
                                          dog_age: int,
                                          expected_res: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_res


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (14, None),
        ("a", "c"),
        ([15], 7),
        ({}, "10")
    ]
)
def test_should_raise_errr_while_invalid_input(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
