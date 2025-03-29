import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, expected_cat_human_age",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (100, 21)
    ]
)
def test_get_cat_age(cat_age: int, expected_cat_human_age: int) -> None:
    cat_human_age = get_human_age(cat_age, 0)[0]
    assert cat_human_age == expected_cat_human_age
