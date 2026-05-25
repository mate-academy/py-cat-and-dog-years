import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dogs_age,expected_result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should convert 0 to 0"
        ),
        pytest.param(
            15,
            5,
            [1, 1],
            id="should convert both to one year"),
        pytest.param(
            27,
            27, [2, 2],
            id="should convert both to two years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should convert to cat's and dog's age appropriately"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should convert large values to cat and dog age appropriately"
        ),
    ]
)


def test_correct_cases(
        cat_age: int,
        dogs_age: int,
        expected_result: list[int, int]
) -> None:
    get_human_age(cat_age, dogs_age)
    assert get_human_age(cat_age, dogs_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dogs_age,expected_error",
    [
        pytest.param(-1, -5, ValueError, id="age should be a positive value"),
        pytest.param(150, 150, ValueError, id="age should be less than 120"),
        pytest.param("cat", "dog", TypeError, id="age should be an integer"),
    ]
)
def test_raised_errors(
        cat_age: int,
        dogs_age: int,
        expected_error: str
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dogs_age)
