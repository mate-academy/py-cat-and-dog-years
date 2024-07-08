import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (
            0,
            0,
            [0, 0]
        ),
        (
            14,
            14,
            [0, 0]
        ),
        (
            15,
            15,
            [1, 1]
        ),
        (
            23,
            23,
            [1, 1]
        ),
        (
            24,
            24,
            [2, 2]
        ),
        (
            27,
            27,
            [2, 2]
        ),
        (
            28,
            28,
            [3, 2]
        ),
        (
            100,
            100,
            [21, 17]
        ),
        (
            10**6,
            10**6,
            [249996, 199997]
        ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (
            -1,
            10,
            [0, 0]
        ),
        (
            10,
            -1,
            [0, 0]
        ),
        (
            -10,
            -10,
            [0, 0]
        ),
    ]
)
def test_get_human_age_invalid_inputs(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == expected), ValueError


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (
            1,
            []
        ),
        (
            [],
            1
        ),
        (
            1,
            {}
        ),
        (
            {},
            1
        ),
        (
            None,
            1
        ),
        (
            1,
            None
        ),
    ]
)
def test_should_raise_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
