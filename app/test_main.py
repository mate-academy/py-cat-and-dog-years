import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (0, -5, None),
        (-4, 2, None),
        (-7, -7, None),
        ("str", [0, 0, 0], None),
        (12.5, 3, None),
        (3, "5", None),
        ("5", None, None),
    ],
    ids=[
        "test cat age and dog age are both years",
        "test cat age and dog age equal one year",
        "test cat age and dog age equal two years",
        "test value slightly less the first limit",
        "test between first and second limit",
        "test on the border of the next block without cat",
        "test on the verge of transition to next block cat gets year",
        "test large number for checking multiple block repetitions",
        "test ValueError is expected:dog's age is negative",
        "test ValueError is expected: cat's age is negative",
        "test ValueError is expected: the ages of both animals are negative",
        "test data TypeError is expected where input cat age is str "
        "and dog age is list",
        "test data TypeError is expected where the code's "
        "value is a decimal number",
        "test data TypeError is expected where the dog's age is String ",
        "test data TypeError is expected where the dog's age None",
    ]
)
def test_valid_values(cat: int, dog: int, result: list[int]) -> None:
    if result is None:
        with pytest.raises(Exception):
            get_human_age(cat, dog)
    else:
        assert get_human_age(cat, dog) == result
