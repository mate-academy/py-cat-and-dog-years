import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "age_cat, age_dog, total",
    [   # if age < 15 result shold to be [0, 0]
        (14, 14, [0, 0]),
        (-25, -18, [0, 0]),
        # check too big arguments
        (500, 10982, [121, 2193]),
        # for arguments 23 result should to be [1, 1]
        (23, 23, [1, 1])
    ]
)
def test_universal(age_cat: int, age_dog: int, total: list) -> None:
    result = get_human_age(age_cat, age_dog)
    assert result == total


def test_is_it_working_propaly() -> None:
    result_1 = get_human_age(20, 32)
    get_human_age(19, 16)
    first_result = get_human_age(20, 32)

    assert result_1 == first_result


def test_if_arguments_is_not_integer() -> None:
    cats_age = {"k": 12}
    dogs_age = {"k": 10}

    with pytest.raises(TypeError):
        get_human_age(cats_age, dogs_age)
