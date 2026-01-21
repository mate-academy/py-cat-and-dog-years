import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            -1, -1, [0, 0],
            id="cat/dog years lesser than zero should return 0"
        ),
        pytest.param(
            0, 0, [0, 0], id="cat/dog years equal to zero should return 0"
        ),
        pytest.param(
            1, 14, [0, 0], id="cat/dog years between 1 and 14 should return 0"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years should convert to 1 human years"
        ),
        pytest.param(
            16, 23, [1, 1],
            id="cat/dog years between 15 and 23 should convert to 1 human year"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years should convert to 2 human years"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="cat/dog years from 16 to 27/28 should convert to 2 human years"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="28/29 cat/dog years should convert to 3 human years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="each 4 years after 28/29 cat/dog years should add 1 human year"
        )
    ]
)
def test_get_human_age_values(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "", "", TypeError,
            id="cat/dog should return TypeError when args type not int"
        )
    ]
)
def test_get_human_age_raises(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
