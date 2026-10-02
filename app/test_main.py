import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="test_zero_ages"),
        pytest.param(14, 14, [0, 0], id="test_before_first_threshold"),
        pytest.param(15, 15, [1, 1], id="test_first_threshold"),
        pytest.param(23, 23, [1, 1], id="test_before_second_threshold"),
        pytest.param(24, 24, [2, 2], id="test_second_threshold"),
        pytest.param(27, 27, [2, 2], id="test_before_cat_increment"),
        pytest.param(28, 28, [3, 2], id="test_cat_increment"),
        pytest.param(100, 100, [21, 17], id="test_large_ages"),
        pytest.param(-1, -1, [0, 0], id="test_negative_ages"),
    ],
)
def test_ages(
    cat_age: int,
    dog_age: int,
    result: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param("15", "15", TypeError, id="string_ages"),
    ],
)
def test_invalid_type(
    cat_age: str,
    dog_age: str,
    error: type[TypeError],
) -> None:
    with pytest.raises(error):
        main.get_human_age(cat_age, dog_age)  # type: ignore[arg-type]
