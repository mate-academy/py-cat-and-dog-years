import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "zero ages cat or dog should be equal zero human year",
        "cat or dog years less than 15 should be equal to 0 human years",
        "1 year from cat or dog should be more or equal 15 and less "
        "or equal 23 human years",
        "2 year from cat should be more or equal 24 and less 28 human years"
        "and 3 year from dog should be more or equal 24 "
        "and less 29 human years",
        "first 15 cat and dog years give 1 human year, next 9 cat "
        "and dog years give 1 more human "
        "year every 4 next cat years (and 5 next dog years) give "
        "1 extra human year.",
        "first 15 cat and dog years give 1 human year, next 9 cat "
        "and dog years give 1 more human "
        "year every 4 next cat years (and 5 next dog years) give "
        "1 extra human year.",

    ]
)
def test_correspondence_of_human_years_to_animals(
        cat_age: int, dog_age: int, human_age: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    ), (f"\'Cat age\' - {cat_age} and \'dog age\' - {dog_age} "
        f"should be equal to {human_age}")
