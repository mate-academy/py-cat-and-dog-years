import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 28, [0, 2]),
        (28, -1, [3, 0]),
        (1000, 1060, [246, 209])
    ],
    ids=[
        "zero for cat and dog years",
        "check border for zero year",
        "check first possible cat/dog age to human age",
        "check border for first year",
        "check lowest possible second year",
        "check border for second year",
        "difference in aging",
        "check if difference gets bigger",
        "negative number for cat_age",
        "negative number for dog_age",
        "enormously big numbers"
    ]
)
def test_check_edging_situations_and_out_of_normal_range_input(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("12", 28),
        (76, "49"),
        ("56", "67"),
        ("", 67)
    ]
)
def test_wrong_type_of_input_for_cat_and_dog_age(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
