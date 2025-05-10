import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_ages",
    [
        pytest.param(14, 14, [0, 0],
                     id="The maximum limit value of which is not enough for 1 human year"),
        pytest.param(15, 15, [1, 1], id="Minimum threshold value for 1 person year"),
        pytest.param(23, 23, [1, 1], id="Maximum threshold value for 1 person year"),
        pytest.param(24, 24, [2, 2], id="Minimum threshold value for 1 more person year"),
        pytest.param(27, 27, [2, 2], id="Average threshold value for 1 more person year"),
        pytest.param(100, 100, [21, 17], id="Different values for each 1 extra year"),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_ages: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_ages
    )
