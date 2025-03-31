import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,exp_human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (128, 129, [28, 23]),
        (99999, 99999, [24995, 19997]),
    ]
)
def test_human_age_boundaries(
    cat_age: int,
    dog_age: int,
    exp_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == exp_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, "15"),
        ("15", 15),
        ([15], 15),
        (15, [15]),
        (15, (15, 13)),
        ((15, 13), 15),
    ]
)
def test_incorrect_type_raises_exception(
    cat_age: any,
    dog_age: any,
) -> None:
    with pytest.raises(TypeError) as ex_info:
        get_human_age(cat_age, dog_age)
    assert ex_info != 0
