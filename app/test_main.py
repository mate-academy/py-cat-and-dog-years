import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0],
                     id="Test for zero values should return result 0"),
        pytest.param(
            14,
            14,
            [0, 0],
            id="Up to the first 15 cat or dog years give 0 human years"),
        pytest.param(
            15,
            15,
            [1, 1],
            id="First 15 cat or dog years give 1 human years"),
        pytest.param(
            24,
            24,
            [2, 2],
            id="Next 9 cat or dog years give plus 1 human years"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Every 4 next cat and 5 dog years add 1 extra human year"),
        pytest.param(
            -1,
            -5,
            [0, 0],
            id="Test for negative values should return 0"),
        pytest.param(
            0,
            0,
            [0, 0],
            id="Test for zero values should return 0"),
        pytest.param(99999, 5555555, [24995, 1111108],
                     id="Test for large numbers, expecting specific values")
    ]
)
def test_get_human_age_with_different_type_of_data(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param("dog", 18, TypeError,
                     id="Test invalid data type, raise exception"),
        pytest.param(18, "dog", TypeError,
                     id="Test invalid data type, raise exception"),
        pytest.param("dog", "dog", TypeError,
                     id="Test invalid data type, raise exception"),
        pytest.param("22", "33", TypeError,
                     id="Test invalid data type, raise exception")
    ]
)
def test_invalid_data_type(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
