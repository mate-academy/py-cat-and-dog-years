import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
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
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-10, -5, [0, 0]),
    ],
)
def test_negative_inputs_treated_as_zero(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,expected_cat",
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
    ],
)
def test_cat_threshold_edges(cat_age: int, expected_cat: int) -> None:
    human_cat, human_dog = get_human_age(cat_age, 0)
    assert human_cat == expected_cat
    assert human_dog == 0


@pytest.mark.parametrize(
    "dog_age,expected_dog",
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 2),
        (30, 3),
    ],
)
def test_dog_threshold_edges(dog_age: int, expected_dog: int) -> None:
    human_cat, human_dog = get_human_age(0, dog_age)
    assert human_cat == 0
    assert human_dog == expected_dog


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15.5, 15),
        ("15", 15),
        (None, 15),
        (15, 15.5),
        (15, "15"),
        (15, None),
    ],
)
def test_incorrect_types_raise_typeerror(cat_age: any, dog_age: any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
