import pytest

from app import main


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
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
def test_get_human_age_should_convert_valid_inputs(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        (-1, -1, [0, 0]),
        (-5, 100, [0, 17]),
        (100, -5, [21, 0]),
    ],
)
def test_get_human_age_should_handle_negative_inputs_as_zero_bucket(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "dog_age"),
    [
        ("1", 1),
        (1, "1"),
        (None, 1),
        (1, None),
        ("1", None),
    ],
)
def test_get_human_age_should_raise_type_error_for_invalid_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
