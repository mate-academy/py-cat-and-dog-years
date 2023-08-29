import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(
        0,
        0,
        [0, 0],
        id="zeros gives zeros"
    ),
    pytest.param(
        14,
        14,
        [0, 0],
        id="Both animals under 15 years should give 0 human age"
    ),
    pytest.param(
        15,
        15,
        [1, 1],
        id="Both animals older 15 years should give 1 human age"
    ),
    pytest.param(
        23,
        23,
        [1, 1],
        id="Both animals under 24 years should give 1 human age"
    ),
    pytest.param(
        24,
        24,
        [2, 2],
        id="Both animals older 24 years should give 2 human age"
    ),
    pytest.param(
        27,
        27,
        [2, 2],
        id="Both animals older 27 years should give 2 human age"
    ),
    pytest.param(
        28,
        28,
        [3, 2],
        id="Cat 28, dog 28 should give 3 and 2 human years respectively"
    ),
    pytest.param(
        29,
        29,
        [3, 3],
        id="Cat 29, dog 29 should give 3 human age"
    ),
    pytest.param(
        99,
        99,
        [20, 17],
        id="Both animals 99 years should give 20 and 17 human age respectively"
    ),
    pytest.param(
        100,
        100,
        [21, 17],
        id="Both animals 100 years should give 21 and 17 human age"
    ),
    pytest.param(
        -1,
        -1,
        [0, 0],
        id="negative age gives 0 human age"
    ),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("0", 0),
        (14, "14"),
        (100, [100]),
    ]
)
def test_get_human_age_correct_value_type(
        cat_age: int,
        dog_age: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
