from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        pytest.param(
            0, 0,
            [0, 0],
            id="test_return_zero_years"
        ),
        pytest.param(
            14, 14,
            [0, 0],
            id="test_return_less_than_15"
        ),
        pytest.param(
            15, 15,
            [1, 1],
            id="test_return_15"
        ),
        pytest.param(
            23, 23,
            [1, 1],
            id="test_return_less_than_24"
        ),
        pytest.param(
            24, 24,
            [2, 2],
            id="test_return_24"
        ),
        pytest.param(
            27, 27,
            [2, 2],
            id="test_cat_dog_age_after_24_years"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="test_cat_and_dog_return_different_result"
        ),
        pytest.param(
            100, 100,
            [21, 17],
            id="test_cat_and_dog_return_big_int_different_result"
        ),
    ]
)
def test_show_cat_dog_to_human_age(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog, expected_exception",
    [
        pytest.param(
            15, -5,
            ValueError,
            id="test on Negative number"
        ),
        pytest.param(
            "5", "5",
            TypeError,
            id="test incorrect data types"
        )
    ]
)
def test_show_expected_exception(
        cat: int,
        dog: int,
        expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat, dog)
