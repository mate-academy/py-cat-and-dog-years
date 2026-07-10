import pytest
from app import main


@pytest.mark.parametrize(
    "cat,dog,expected",
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
def test_examples(cat: int, dog: int, expected: list[int]) -> None:
    assert main.get_human_age(cat, dog) == expected


@pytest.mark.parametrize(
    "age,cat_expected", [(14, 0), (15, 1), (23, 1), (24, 2)]
)
def test_cat_boundaries(age: int, cat_expected: int) -> None:
    assert main.get_human_age(age, 0)[0] == cat_expected


@pytest.mark.parametrize(
    "age,dog_expected", [(14, 0), (15, 1), (23, 1), (24, 2)]
)
def test_dog_boundaries(age: int, dog_expected: int) -> None:
    assert main.get_human_age(0, age)[1] == dog_expected


def test_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        main.get_human_age(-1, 0)
    with pytest.raises(ValueError):
        main.get_human_age(0, -1)


def test_incorrect_type_raises_type_error() -> None:
    with pytest.raises(TypeError):
        main.get_human_age(1.5, 0)
    with pytest.raises(TypeError):
        main.get_human_age(0, "1")
