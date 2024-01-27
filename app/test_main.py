import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(14, 14, [0, 0],
                     id="up to the first 15 cat/dog years give 0 human years"),
        pytest.param(15, 15, [1, 1],
                     id="first 15 cat years give 1 human year"),
        pytest.param(24, 24, [2, 2],
                     id="the next 9 cat/dog years give 1 more human year"),
        pytest.param(100, 100, [21, 17],
                     id="4 cat years and 5 dog years add 1 extra human year"),
        pytest.param(-5, -6, [0, 0],
                     id="test for negative values, should return 0"),
        pytest.param(0, 0, [0, 0],
                     id="test for zero values, should return 0"),
        pytest.param(99999, 5555555, [24995, 1111108],
                     id="test for large numbers, expecting specific values")
    ]
)
def test_get_human_age_with_different_type_of_data(
    cat_age: int,
    dog_age: int,
    expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("cat_age, dog_age, expected_error", [
    pytest.param("cat", 10, TypeError,
                 id="test invalid data type, raise exception."),
    pytest.param(10, "dog", TypeError,
                 id="test invalid data type, raise exception."),
    pytest.param("cat", "dog", TypeError,
                 id="test invalid data type, raise exception."),
    pytest.param("24", "24", TypeError,
                 id="test invalid data type, raise exception."),
])
def test_incorrect_type_of_data_error(
    cat_age: int,
    dog_age: int,
    expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
