import pytest

from app import main


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
        (-1, 5, [0, 0]),
        (5, -3, [0, 0]),
        (0, 15, [0, 1]),
        (15, 0, [1, 0]),
    ],
    ids=[
        "zeros",
        "below_first_threshold",
        "first_human_year_both",
        "still_one_human_year_both",
        "second_human_year_both",
        "cat_dog_same_before_cat_extra_step",
        "cat_three_dog_two_at_28",
        "large_ages",
        "negative_cat_age",
        "negative_dog_age",
        "asymmetric_zero_and_fifteen",
        "asymmetric_fifteen_and_zero",
    ],
)
def test_get_human_age_examples_and_edges(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 24, [1, 2]),
        (24, 23, [2, 1]),
    ],
    ids=[
        "cat_one_below_dog_at_first_threshold",
        "cat_at_first_dog_one_below",
        "cat_one_below_second_dog_at_second",
        "cat_at_second_dog_one_below",
    ],
)
def test_mixed_ages_cross_species_boundaries(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "bad_cat,bad_dog",
    [
        ("15", 1),
        (1, 3.5),
        (None, 1),
        (1, []),
    ],
    ids=["cat_str", "dog_float", "cat_none", "dog_list"],
)
def test_invalid_types_raise_type_error(
    bad_cat: object,
    bad_dog: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(bad_cat, bad_dog)
