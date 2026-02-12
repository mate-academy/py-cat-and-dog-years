# flake8: noqa: *
import pytest

from app.main import get_human_age
from app.errors import OutOfRangeError

@pytest.mark.parametrize(
    'human_cat_age,human_dog_age,expected_result',
    [
        pytest.param(0, 0, [0, 0], id="Ages 0"),
        pytest.param(14, 14, [0, 0], id="0 < Ages < 15"),
        pytest.param(15, 15, [1, 1], id="Ages == 15"),
        pytest.param(23, 23, [1, 1], id="15 < Ages < 24"),
        pytest.param(24, 24, [2, 2], id="Ages == 24"),
        pytest.param(28, 28, [3, 2], id="Ages > 24"),
        pytest.param(100, 100, [21, 17], id="Ages large number"),
    ])
def test_logic_for_different_ages(human_cat_age, human_dog_age, expected_result) -> None:
    assert get_human_age(human_cat_age, human_dog_age) == expected_result


@pytest.mark.parametrize(
    'human_cat_age,human_dog_age,expected_result',
    [
        pytest.param(-13, 13, OutOfRangeError, id="Negative cat"),
        pytest.param(13, -13, OutOfRangeError, id="Negative dog"),
        pytest.param(10, 222, OutOfRangeError, id="Large dog"),
        pytest.param(222, 10, OutOfRangeError, id="large cat"),
        pytest.param("2222", 2222, TypeError, id="Wrong type of cat"),
        pytest.param(2222, "2222", TypeError, id="Wrong type of dog"),
    ])
def test_logic_for_incorrect_numbers(human_cat_age, human_dog_age, expected_result) -> None:
    with pytest.raises(expected_result):
        get_human_age(human_cat_age, human_dog_age)