import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "first_year,second_year,result",
    [
        (0, 0, [0, 0]),

        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (1000, 1000, [246, 197]),
        (-1, -1, [0, 0]),
    ]
)
def test_get_human_age(first_year: int,
                       second_year: int,
                       result: list[int]) -> None:
    assert get_human_age(first_year, second_year) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("10", 10),
        (10, "10"),
        (10.5, 10),
        (10, 10.5),
    ]
)
def test_get_human_age_raises_type_error_when_age_is_not_int(
    cat_age: object,
    dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
