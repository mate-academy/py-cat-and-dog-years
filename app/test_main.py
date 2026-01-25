import pytest
from app import main


@pytest.mark.parametrize(
    "num1,num2",
    [
        ([6], [5]),
        (67.5, 34.93),
        (26, 89.4),
        (3.45, 0),
        (True, False),
        ("4", "5"),
    ],
)
def test_data_inputs_are_integers(
    num1: int,
    num2: int,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(num1, num2)


@pytest.mark.parametrize(
    "num1,num2",
    [
        (-5, 6),
        (34, -7),
        (-3, -76),
    ],
)
def test_data_inputs_are_naturals(
    num1: int,
    num2: int,
) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(num1, num2)


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (32, 32, [4, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_animal_age_to_human_years(num1: int, num2: int, result: list) -> None:
    assert main.get_human_age(num1, num2) == result, (
        f"The human age for a dog with {num2} years is {result[1]}"
        f" and the human age for a cat with {num1} years is {result[0]}"
    )
