import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="zero age should return list with zeros"
        ),
        pytest.param(
            -5, -1, [0, 0],
            id="negative age should return list with zeros"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="age less then 15 should return list with zeros"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="the age of both animals coincides with 1 human year"
        ),
        pytest.param(
            27, 2, [2, 0],
            id="only one of animal age is less than 1 human year"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="the same age for animals can return different human age"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="check the big ages"
        ),
        pytest.param(
            1024, 1024, [252, 202],
            id="check the big ages"
        )
    ]
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
        ({3}, 3, TypeError),
        (100, [100], TypeError),
        ("1", 1, TypeError)
    ]
)
def test_type_of_value_for_human_age(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
