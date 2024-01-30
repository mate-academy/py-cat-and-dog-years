import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    pytest.param(0, 0, [0, 0], id="Zero Ages"),
    pytest.param(14, 14, [0, 0], id="Equal Ages"),
    pytest.param(15, 15, [1, 1], id="Cat 15, Dog 15"),
    pytest.param(23, 23, [1, 1], id="Cat 23, Dog 23"),
    pytest.param(24, 24, [2, 2], id="Cat 24, Dog 24"),
    pytest.param(27, 27, [2, 2], id="Cat 27, Dog 27"),
    pytest.param(28, 28, [3, 2], id="Cat 28, Dog 28"),
    pytest.param(100, 100, [21, 17], id="Cat 100, Dog 100")
])
def test_get_human_age(cat_age, dog_age, expected_result):
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("cat_age,dog_age,expected_error", [
    pytest.param("10", 5, TypeError, id="String cat age"),
    pytest.param("cat", "dog", TypeError, id="String cat and dog Ages"),
])
def test_get_human_exceptions(cat_age, dog_age, expected_error):
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
