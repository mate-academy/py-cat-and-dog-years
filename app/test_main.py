import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return '[0, 0]' when ages are negative"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return '[0, 0]' when ages are '0'"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return '[0, 0]' when ages are less then '15'",
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return '[1, 1]' when ages are '15'"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return '[1, 1]' when ages are '23'"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return '[2, 2]' when ages are '24'"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return '[2, 2]' when ages are '27'"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="should return '[2, 2]' when cat age are ' 27' "
               "and dog age are '28'",
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return '[3, 2]' when ages are '28'"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return '[3, 3]' when cat age are '28' "
               "and dog age are '29'",
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return '[21, 17]' when cat age are '100' "
               "and dog age are '100'",
        ),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("15", 15, TypeError),
        (15, "15", TypeError),
        ([15], 15, TypeError),
        ({15}, 15, TypeError),
    ]
)
def test_error_when_incorrect_value(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
