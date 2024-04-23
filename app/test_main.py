import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (23, 23, [1, 1]),
        (14, 14, [0, 0]),
        (15.5, 15.1, [1, 1])
    ]
)
def test_of_correct_counting(cat: int, dog: int, expected: list) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        pytest.param(1000, 150, ValueError, id='extremely large value'),
        pytest.param(-5, 12, ValueError, id='zero value'),
        pytest.param(0, -100, ValueError, id='negative value')
    ]
)
def test_should_raise_error_when_data_out_of_normal_range(cat, dog, expected) -> None:
    with pytest.raises(expected):
        get_human_age(cat, dog)


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        pytest.param({}, 12, TypeError, id='dict input'),
        pytest.param([], 0, TypeError, id='list input'),
        pytest.param(set(), 21, TypeError, id='set input'),
        pytest.param("one", 15, TypeError, id='string input'),
    ]
)
def test_should_raise_error_when_input_data_not_a_number(cat, dog, expected) -> None:
    with pytest.raises(expected):
        get_human_age(cat, dog)
