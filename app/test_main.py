import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_converted_years",
    [
        pytest.param(
            14, 14, [0, 0],
            id="14 cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="23 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="27/28 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="28/29 cat/dog years should convert into 3 human age"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should return zero if cat/dog age is zero"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="should return zero if cat/dog age is negative"
        ),
        pytest.param(
            1_000_000, 1_000_000, [249996, 199997],
            id="should works correctly with big ages"
        )
    ]
)
def test_convert_years_correctly(
        cat_age: int,
        dog_age: int,
        expected_converted_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_converted_years


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            "1", "2",
            id="str TypeError"
        ),
        pytest.param(
            None, None,
            id="None TypeError"
        ),
    ]
)
def test_type_err_exceptions(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
