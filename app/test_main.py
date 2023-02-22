import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(1, 1, [0, 0], id="both animals younger than 15 years"),
        pytest.param(15, 15, [1, 1], id="both animals 15 years old"),
        pytest.param(23, 23, [1, 1], id="both animals 23 years old"),
        pytest.param(27, 28, [2, 2], id="cat 27, dog 28 years old"),
        pytest.param(14, 14, [0, 0], id="both animals 14 years old"),
        pytest.param(28, 29, [3, 3], id="cat 28, dog 29 years old"),
    ],
)
def test_get_human_age(cat_age, dog_age, expected_result):
    assert get_human_age(cat_age, dog_age) == expected_result
