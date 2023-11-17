import pytest
from app.main import get_human_age


def test_should_raise_typerror() -> None:
    with pytest.raises(TypeError):
        get_human_age("age is 15", 11)


@pytest.mark.parametrize(
    "dog_age,cat_age,expected",
    [
        (-3, -11, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (500, 500, [121, 97])
    ]
)
def test_should_return_expected_results(
    dog_age: int,
    cat_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
