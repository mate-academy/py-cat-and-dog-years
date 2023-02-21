import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="zero_test"),
        pytest.param(3, 3, [0, 0], id="young_age_test"),
        pytest.param(100, 85, [21, 14], id="old_age_test"),
        pytest.param(-2, 28, [0, 2], id="minus_cat_age_test"),
        pytest.param(-2, -5, [0, 0], id="minus_cat_and_dog_age_test"),
        pytest.param(0, -28, [0, 0], id="cat_zero_and_minus_dog_age_test"),

    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("28", 100, id="type_error_string_instead_of_integer"),
        pytest.param([1], 100, id="type_error_list_instead_of_integer"),
        pytest.param({}, 100, id="type_error_dict_instead_of_integer"),
    ]
)
def test_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
