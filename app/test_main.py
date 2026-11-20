import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age_cat,age_dog,result_list",
    [
        pytest.param(-1, -1, [0, 0]),
        pytest.param(-100, -50, [0, 0]),
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 24, [2, 2]),
        pytest.param(28, 24, [3, 2]),
        pytest.param(27, 28, [2, 2]),
        pytest.param(28, 29, [3, 3]),
        pytest.param(1000, 1000, [246, 197])
    ]
)
def test_get_human_age(age_cat: int, age_dog: int, result_list: list) -> None:
    assert get_human_age(age_cat, age_dog) == result_list, \
        f"{age_cat}, {age_dog} - {result_list} error results"


@pytest.mark.parametrize(
    "age_cat,age_dog,error_results",
    [
        pytest.param("1000", 1000, TypeError),
        pytest.param(1000, "1000", TypeError)
    ]
)
def test_get_human_age_raises_type_error(
        age_cat: int,
        age_dog: int,
        error_results: type[TypeError]) -> None:
    with pytest.raises(TypeError):
        get_human_age(age_cat, age_dog)
