import pytest

from app.main import get_human_age


def test_should_return_list_of_two_elements() -> None:
    assert len(get_human_age(10, 10)) == 2, (
        "Result should contain exactly two elements: [cat, dog]"
    )


def test_cat_age_converted_independently_from_dog_age() -> None:
    assert get_human_age(15, 0) == [1, 0], (
        "Cat age should be converted independently from dog age"
    )


def test_dog_age_converted_independently_from_cat_age() -> None:
    assert get_human_age(0, 15) == [0, 1], (
        "Dog age should be converted independently from cat age"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "negative ages give zero human years",
        "zero ages give zero human years",
        "ages below 15 give zero human years",
        "first 15 years give 1 human year",
        "ages below 24 still give 1 human year",
        "next 9 years give 1 more human year",
        "remainder is discarded before full step",
        "cat gets extra year every 4 years",
        "dog gets extra year every 5 years",
        "big ages",
    ],
)
def test_get_human_age_boundary_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected, (
        f"get_human_age({cat_age}, {dog_age}) "
        f"should return {expected}"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
    ],
    ids=[
        "cat age as string",
        "dog age as string",
        "cat age as None",
        "dog age as None",
    ],
)
def test_incorrect_types_should_raise_type_error(
    cat_age: int | str | None,
    dog_age: int | str | None,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
