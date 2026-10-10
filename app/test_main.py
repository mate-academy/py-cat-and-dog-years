import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197])
    ]
)
def test_animal_age_conversion_to_human_age(
    cat_age: int, dog_age: int, human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (-1, -1, [0, 0]),
        (-1000, -1000, [0, 0]),
    ]
)
def test_animal_age_with_negative_numbers(
    cat_age: int, dog_age: int, human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    (
        ["15", "15"],
        [15.5, 16]
    )
)
def test_type_of_cat_and_dog_ages(cat_age: any, dog_age: any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
