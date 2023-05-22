import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 15, [0, 1]),
        (14, -2, [0, 0]),
        (-15, -15, [0, 0]),
        (28, -28, [3, 0]),
        (14.5, 23.2, [0, 1]),
        (30, True, [3, 0])
    ],
    ids=[
        "function should return 0 if the age of the animals is 0",
        "function should return 0 if the age of the animals < 15",
        "function should return 1 if the age of the animals 15",
        "function should return 1 if the age of the animals < 24",
        "function should return 2 if the age of the animals 24",
        "function should return 2 if the age of the animals < 27",
        "function should correctly count the age of dogs and cats over 28",
        "function should correctly count the age of dogs and cats over 28",
        "function should return 0 if input less then 0",
        "function should return 0 if input less then 0",
        "function should return 0 if input less then 0",
        "function should return 0 if input less then 0",
        "function should work even if input is float type",
        "function should return 0 if input is bool"
    ]
)
def test_get_human_age(cat_years: int, dog_years: int, result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        ("12", 15),
        (23, [10, 20]),
        (None, 15),
        ({"cat": 15}, {"dog": 18}),
        (23, {23})
    ]
)
def test_should_return_error_if_input_has_wrong_type(
        cat_years: str | int | dict[str, int] | None,
        dog_years: int | list[int] | dict[str, int] | set[int]
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
