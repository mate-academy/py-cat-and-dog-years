from app.main import get_human_age
import pytest


def test_must_return_two_elements() -> None:
    assert len(get_human_age(13, 13)) == 2


def test_all_elements_of_return_array_must_be_int() -> None:
    result = get_human_age(11, 11)
    assert isinstance(result[0], int) and isinstance(result[1], int)


def test_should_raise_error() -> None:
    with pytest.raises(TypeError):
        get_human_age([1, 2], [3, 4])


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(-10, -10, [0, 0], id="if age < 0"),
        pytest.param(0, 0, [0, 0], id="if age is 0"),
        pytest.param(14, 14, [0, 0], id="if age < 15"),
        pytest.param(15, 15, [1, 1], id="if age >= 15"),
        pytest.param(23, 23, [1, 1], id="if age <= 23"),
        pytest.param(24, 24, [2, 2], id="if age >= 24"),
        pytest.param(27, 27, [2, 2], id="if age <= 27"),
        pytest.param(28, 28, [3, 2], id="if age >= 28"),
        pytest.param(100, 100, [21, 17], id="if age == 100"),
        pytest.param(10000, 10000, [2496, 1997], id="if age == 10000"),
    ]
)
def test_converted_to_human_years(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
