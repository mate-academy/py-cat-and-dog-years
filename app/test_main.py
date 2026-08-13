import pytest


from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 24, [1, 2]),
        (24, 23, [2, 1]),
        (27, 28, [2, 2]),
        (28, 27, [3, 2]),
        (29, 29, [3, 3]),
    ],
)
def test_boundary_conditions(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-10, -10),
    ],
)
def test_should_raise_error_for_negative_ages(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
    ],
)
def test_should_raise_error_for_incorrect_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (1000, 1000),
        (10000, 10000),
        (100000, 100000),
    ],
)
def test_should_handle_large_numbers(
    cat_age: int,
    dog_age: int,
) -> None:
    result = main.get_human_age(cat_age, dog_age)

    assert result[0] == 2 + (cat_age - 24) // 4
    assert result[1] == 2 + (dog_age - 24) // 5
