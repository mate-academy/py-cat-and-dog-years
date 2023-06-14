import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ([2], 8, TypeError),
        (10, [1], TypeError),
        ("hello", "13", TypeError)
    ]
)
def test_raise_error_if_value_types_are_incorrect(
        cat_age: int | list | str,
        dog_age: int | list | str,
        error: type[Exception]
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            2,
            8,
            [0, 0],
            id="age should be zero when ages below 15"
        ),
        pytest.param(
            16,
            19,
            [1, 1],
            id="age should be one when ages between 15 and 23"
        ),
        pytest.param(
            24,
            27,
            [2, 2],
            id="age should be one when ages between 23 and 28"
        ),
        pytest.param(
            -1,
            -10,
            [0, 0],
            id="age should be zero when ages is negative numbers"
        ),
        pytest.param(
            14,
            35,
            [0, 4],
            id="age in other cases"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zero when ages equals zero"
        ),
        pytest.param(
            12351162626,
            123124343573,
            [3087790652, 24624868711],
            id="should work correctly with large numbers"
        )
    ]
)
def test_age_converts_correctly(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
