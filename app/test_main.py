import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "result"),
    [
        (0, 0, 0),
        (14, 14, 0),
        (15, 15, 1),
        (23, 23, 1),
        (24, 24, 2),
        (27, 28, 2),
        (28, 29, 3)
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: int
) -> None:
    assert set(get_human_age(cat_age, dog_age)) == {result}
