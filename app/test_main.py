import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("cat", "dog"),
        (1, "dog"),
        ("cat", 13),
        (None, None),
        (1, None),
        (None, 6),
    ]
)
def test_should_raise_type_error_when_arguments_are_not_numbers(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, -1),
        (-23, 10),
        (10, -23),
        (-14, -14),
        (-3, 14),
        (0, 0),
        (3, 10),
        (10, 3),
        (13, 3),
        (3, 13),
        (0, 14),
        (14, 0),
        (14, 14),
    ]
)
def test_human_years_should_be_0_for_animal_age_below_15(
    cat_age: int,
    dog_age: int
) -> None:
    cat_to_human, dog_to_human = get_human_age(cat_age, dog_age)
    assert cat_to_human == 0 and dog_to_human == 0, (
        "Human years must be 0 for animal ages < 15"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, 15),
        (18, 22),
        (23, 16),
        (15, 23),
        (23, 15),
        (23, 23),
    ]
)
def test_human_years_should_be_1_for_animal_ages_from_15_to_24(
    cat_age: int,
    dog_age: int
) -> None:
    cat_to_human, dog_to_human = get_human_age(cat_age, dog_age)
    assert cat_to_human == 1 and dog_to_human == 1, (
        "Human years must be 1g for animal ages < 24"
    )


@pytest.mark.parametrize(
    "dog_age,expected",
    [
        (24, 2),
        (27, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (98, 16),
        (99, 17),
    ]
)
def test_dog_to_human_years_calculation_age_24_and_after(
    dog_age: int, expected: int
) -> None:
    _, dog_to_human = get_human_age(1, dog_age)
    assert dog_to_human == expected, (
        "Every 5 years after dog age == 24 should count as a human year"
    )


@pytest.mark.parametrize(
    "cat_age,expected",
    [
        (24, 2),
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (33, 4),
        (99, 20),
        (100, 21),
    ]
)
def test_cat_to_human_years_calculation_age_24_and_after(
    cat_age: int,
    expected: int
) -> None:
    cat_to_human, _ = get_human_age(cat_age, 1)
    assert cat_to_human == expected, (
        "Every 4 years after cat age == 24 should count as a human year"
    )
