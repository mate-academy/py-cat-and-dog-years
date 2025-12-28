import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_human_age,dog_human_age",
    [
        pytest.param(0, 0, 0, 0, id="both_zero"),
        pytest.param(14, 5, 0, 0, id="cat_14_dog_5_result_zero"),
        pytest.param(15, 15, 1, 1, id="both_15_result_1"),
        pytest.param(23, 23, 1, 1, id="both_23_result_1"),
        pytest.param(24, 24, 2, 2, id="both_24_result_2"),
        pytest.param(28, 28, 3, 2, id="cat_28_dog_28_result_3_and_2"),
        pytest.param(100, 100, 21, 17, id="cat_100_dog_100_result_21_and_17"),
    ])
def test_get_human_age(cat_age: int, dog_age: int,
                       cat_human_age: int, dog_human_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == [cat_human_age, dog_human_age]
