import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        pytest.param(23, 23, [1, 1], id="one years"),
        pytest.param(14, 14, [0, 0], id="zero years"),
        pytest.param(15.5, 15.1, [1, 1], id="floating input"),
        pytest.param(-5, -100, [0, 0], id="negative value"),
        pytest.param(0, 0, [0, 0], id="zeros input"),
        pytest.param(100, 100, [21, 17], id="big values input")

    ]
)
def test_of_correct_counting(cat: int, dog: int, expected: list) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        pytest.param({}, 12, TypeError, id="dict input"),
        pytest.param([], 0, TypeError, id="list input"),
        pytest.param(set(), 21, TypeError, id="set input"),
        pytest.param("one", 15, TypeError, id="string input"),
    ]
)
def test_should_raise_error_when_input_data_not_a_number(
        cat: int,
        dog: int,
        expected: Exception
) -> None:
    with pytest.raises(expected):
        get_human_age(cat, dog)
