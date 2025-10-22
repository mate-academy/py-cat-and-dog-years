import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0,0]),
        (14, 14, [0,0]),
        (15, 15, [1,1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (50, 40, [8,5]),
        (-1, -10, [0, 0]),
    ],
)

def test_get_human_age_scenarios(cat_age: int,
                                 dog_age: int,
                                 expected: list[int]
                                 ):
    assert get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "invalid_cat_age, invalid_dog_age",
    [
        ("a", 10),
        (10, "b"),
        (1.5, 10),
        (10, 2.5),
        ([1], 10),
        (10, {"age": 5}),
    ]
)
def test_get_human_age_invalid_inputs(invalid_cat_age,
                                        invalid_dog_age
                                        ):
    with pytest.raises(TypeError):
        get_human_age(invalid_cat_age, invalid_dog_age)
