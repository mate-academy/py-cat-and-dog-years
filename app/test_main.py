import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "first_year,second_year,each_year_cat,each_year_dog",
    [
        (-50, 0, 0, 0),
        (14.9, 14.9, 0, 0),
        (14, 15, 0, 1),
        (1000, 1000, 246, 197),
        (28, 28, 3, 2)
    ],
    ids=[
        "If negative or 0 cat/dog years should convert into 0 human age.",
        "If float cat/dog years should convert into correct human age.",
        "Test correct value for the next human year.",
        "Test for a large age.",
        "Test for a correct value for a dog year.",
    ]
)
def test_get_human_age_returns_correct_human_age_with_different_args(
        first_year: int,
        second_year: int,
        each_year_cat: int,
        each_year_dog: int) -> None:
    assert (get_human_age(first_year, second_year)
            == [each_year_cat, each_year_dog])


@pytest.mark.parametrize(
    "first_year,second_year, error",
    [
        ("Tommy", -32, TypeError),
        (14, "14", TypeError),
    ],
    ids=[
        "It should raise TypeError if parameter is not int/float.",
        "It should raise TypeError if parameter can to int()",
    ]
)
def test_get_human_age_raises_type_error_when_args_are_not_int(
        first_year: int,
        second_year: int,
        error: TypeError) -> None:
    with pytest.raises(TypeError):
        assert get_human_age(first_year, second_year)
