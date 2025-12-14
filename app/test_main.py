from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0])
    ],
    ids=[
        "cat: 0, dog: 0",
        "cat: 14, dog: 14",
    ]
)
def test_return_0_for_age_less_than_15(
    cat_years: int,
    dog_years: int,
    expected: list[int]
) -> None:
    actual = get_human_age(cat_years, dog_years)
    assert (actual == expected), (
        "15 cat/dog years equal to 1 human year. "
        f"Received: {actual}, when expected: {expected}"
    )


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1])
    ],
    ids=[
        "cat: 15, dog: 15",
        "cat: 23, dog: 23",
    ]
)
def test_return_1_for_age_between_15_and_23(
    cat_years: int,
    dog_years: int,
    expected: list[int]
) -> None:
    actual = get_human_age(cat_years, dog_years)
    assert (actual == expected), (
        "Function should return 1 for age between 15 and 23. "
        f"Received: {actual}, when expected: {expected}"
    )


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2])
    ],
    ids=[
        "cat: 24, dog: 24",
        "cat: 27, dog: 27",
    ]
)
def test_return_2_for_age_between_24_and_27(
    cat_years: int,
    dog_years: int,
    expected: list[int]
) -> None:
    actual = get_human_age(cat_years, dog_years)
    assert (actual == expected), (
        "Function should return 2 for age between 24 and 27. "
        f"Received: {actual}, when expected: {expected}"
    )


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "cat: 28, dog: 28",
        "cat: 100, dog: 100",
    ]
)
def test_return_correct_value_for_age_more_than_27(
    cat_years: int,
    dog_years: int,
    expected: list[int]
) -> None:
    actual = get_human_age(cat_years, dog_years)
    assert (actual == expected), (
        "Function should return correct value for age more than 27. "
        f"Received: {actual}, when expected: {expected}"
    )


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        (28, 28)
    ],
    ids=[
        "cat and dog params should be unchanged"
    ]
)
def test_initial_parameters_should_not_be_changed_by_function(
    cat_years: int,
    dog_years: int
) -> None:
    old_cat_years = cat_years
    old_dog_years = dog_years
    get_human_age(cat_years, dog_years)
    assert (
        cat_years == old_cat_years and old_dog_years == dog_years
    ), "Initial parameters should stay unchanged"


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        (-2, 10),
        (10, 220)
    ],
    ids=[
        "animal age negative int",
        "animal age too big number"
    ]
)
def test_should_raise_error_for_invalid_input_years_value(
    cat_years: int,
    dog_years: int
) -> None:
    with pytest.raises(ValueError) as e:
        get_human_age(cat_years, dog_years)
    assert str(e.value) == "Only age between 0 and 100 is accepted"


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        ("2", 10),
        (10, [7])
    ],
    ids=[
        "string in as cat age",
        "list as dog age"
    ]
)
def test_should_raise_error_for_invalid_input_years_type(
    cat_years: int,
    dog_years: int
) -> None:
    with pytest.raises(TypeError) as e:
        get_human_age(cat_years, dog_years)
    assert str(e.value) == "Only 'int' type as accepted as input"
