import pytest

from app.main import get_human_age


def test_get_human_age_returns_list() -> None:
    assert (isinstance(get_human_age(1, 7), list))


def test_raises_exception_if_str() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", "")


def test_raises_exception_if_float() -> None:
    with pytest.raises(TypeError):
        get_human_age(0.1, 2.325)


def test_raises_exception_if_list() -> None:
    with pytest.raises(TypeError):
        get_human_age([1, 2], [2, 3])


def test_raises_exception_if_bool() -> None:
    with pytest.raises(TypeError):
        get_human_age(True, False)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(-1, -2, id="Input cannot be negative"),
        pytest.param(0, 0, id="Input cannot be 0"),
        pytest.param(200, 200, id="Input cannot be really large numbers")
    ]
)
def test_input_int_out_of_normal_range(cat_age: int, dog_age: int):
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(1, 1, [0, 0], id="Cat and dog age == 1"),
        pytest.param(14, 14, [0, 0], id="Cat and dog age == 14"),
        pytest.param(1, 15, [0, 1], id="Cat == 0 and dog == 15"),
        pytest.param(15, 15, [1, 1], id="Cat and dog age == 15"),
        pytest.param(23, 23, [1, 1], id="Cat and dog age == 23"),
        pytest.param(24, 24, [2, 2], id="Cat and dog age == 24"),
        pytest.param(27, 27, [2, 2], id="Cat and dog age == 27"),
        pytest.param(28, 28, [3, 2], id="Cat and dog age == 28"),
        pytest.param(100, 100, [21, 17], id="Cat and dog age == 100"),
    ]
)
def test_returns_correct_values(
        cat_age: int,
        dog_age: int,
        expected: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )
