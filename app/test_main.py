import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="both ages equal 0"),
        pytest.param(14, 14, [0, 0], id="both ages less then 15"),
        pytest.param(15, 15, [1, 1], id="both ages equal 15"),
        pytest.param(23, 23, [1, 1], id="both ages less then 15 + 9"),
        pytest.param(24, 24, [2, 2], id="both ages equal 15 + 9"),
        pytest.param(27, 28, [2, 2], id="cat's age less then (15 + 9 + 4), "
                                        "dog's age less then (15 + 9 + 5)"),
        pytest.param(28, 29, [3, 3], id="cat's age equals (15 + 9 + 4), "
                                        "dog's age equals (15 + 9 + 5)"),
        pytest.param(29, 30, [3, 3], id="cat is older then (15 + 9 + 4), "
                                        "dog is older then (15 + 9 + 5)"),
        pytest.param(100, 100, [21, 17], id="both ages are very high = 100"),
        pytest.param(-1, -1, [0, 0], id="both ages are less then 0")
    ]
)
def test_get_human_age_works_correctly(
        cat_age: int,
        dog_age: int,
        result: int) -> None:
    assert (get_human_age(cat_age, dog_age) == result
            ), (f"Result converting cat's age {cat_age}"
                f" and dog's age {dog_age} should be equal to {result}")


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param("1", 0, TypeError, id="cat's age is integer"),
        pytest.param(1, [0], TypeError, id="dog's age is integer")
    ]
)
def test_get_human_age_raise_error_if_age_is_not_int(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
