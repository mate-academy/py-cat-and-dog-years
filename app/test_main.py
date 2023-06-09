import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(1, 1, [0, 0], id="both animals younger than 15 years"),
        pytest.param(25, 25, [2, 2], id="both animals older "
                                        "than 15 + 9 years"),
        pytest.param(15, 15, [1, 1], id="both animals 15 years old"),
        pytest.param(23, 23, [1, 1], id="both animals 23 years old"),
        pytest.param(24, 24, [2, 2], id="both animals 24 years old"),
        pytest.param(27, 28, [2, 2], id="cat 27, dog 28 years old"),
        pytest.param(14, 14, [0, 0], id="both animals 14 years old"),
        pytest.param(28, 29, [3, 3], id="cat 28, dog 29 years old"),
        pytest.param(-1, -1, [0, 0], id="both animals have negative ages"),
        pytest.param(100, 200, [21, 37], id="cat 100, dog 200 years old"),
    ],
)
def test_get_human_age(
        cat_age: int, dog_age: int, expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_get_human_age_if_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("20", [20])
