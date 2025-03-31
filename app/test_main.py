import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0], id="zero age value should return 0"
        ),
        pytest.param(
            100, 100, [21, 17], id="too big ages values"
        ),
        pytest.param(
            14, 14, [0, 0], id="cat/dog age is less than "
                               "1 human's year"
        ),
        pytest.param(
            15, 15, [1, 1], id="14 cat/dog years is equals to "
                               "1 for human years"
        ),
        pytest.param(
            23, 23, [1, 1], id="15 cat/dog years is equals to "
                               "1 for human year"
        ),
        pytest.param(
            24, 24, [2, 2], id="24 cat/dog years is equals to "
                               "2 for human years"
        ),
        pytest.param(
            27, 27, [2, 2], id="27 cat/dog years is equals to "
                               "2 for human years"
        ),
        pytest.param(
            28, 28, [3, 2], id="28 cat years is equals to "
                               "3 for human years and "
                               "28 dog years is equals to "
                               "2 for human years"
        ),
        pytest.param(
            29, 29, [3, 3], id="3 human years is equal to 29 for a cat/dog"
        ),
        pytest.param(
            -3, -3, [0, 0], id="negative age value should return 0"
        ),
    ],
)
def test_correct_getting_human_age(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("14", 14, TypeError),
        (23, "23", TypeError),
        ({28}, 28, TypeError),
        (27, [27], TypeError)
    ]
)
def test_type_of_value_for_human_age(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
