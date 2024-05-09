from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,converted_age_list", [
        pytest.param(0, 0, [0, 0], id="zeros"),
        pytest.param(14, 14, [0, 0], id="boundary less then one"),
        pytest.param(15, 15, [1, 1], id="boundary more then one"),
        pytest.param(23, 23, [1, 1], id="boundary less than two"),
        pytest.param(24, 24, [2, 2], id="boundary more than two"),
        pytest.param(27, 27, [2, 2], id="boundary less than three for cat"),
        pytest.param(28, 28, [3, 2], id="boundary more than three for cat "
                                        "and less than three for dog"),
        pytest.param(100, 100, [21, 17], id="one hundred for each"),
        pytest.param(24.5, 30.5, [2, 3], id="float values"),
        pytest.param(-1, -228, [0, 0], id="negative values"),
        pytest.param(300, 300, [71, 57], id="out of normal range data"),
    ]
)
def test_get_human_age_boundary_values(
        cat_age: int,
        dog_age: int,
        converted_age_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == converted_age_list
