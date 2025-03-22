import pytest

from app.main import get_human_age


def test_raises_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("kitten", 5)


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-1, 0, [0, 0]),
        (13, 14, [0, 0]),
        (20, 22, [1, 1]),
        (24, 25, [2, 2]),
        (30, 36, [3, 4]),
        (120, 120, [26, 21])
    ],
    ids=[
        "not positive numbers should return [0, 0]",
        "test zero human years",
        "test one human year",
        "test two human years",
        "test different human years for cat and dog",
        "test wih big numbers",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
