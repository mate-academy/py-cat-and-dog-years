import pytest
from app.main import get_human_age


@pytest.mark.parametrize("input_cat_age,input_dog_age,expected_output", [
    pytest.param(0, 0, [0, 0],
                 id="Should return zero if cat or dog age are zeros"),
    pytest.param(14, 14, [0, 0],
                 id="Should return zero if cat or dog age less than 14"),
    pytest.param(15, 15, [1, 1],
                 id="Should return one if cat or dog age greater than 14"),
    pytest.param(23, 23, [1, 1],
                 id="Should return one if cat or dog age equal to 23"),
    pytest.param(100, 100, [21, 17],
                 id="Should return correct values "
                    "if cat or dog age less than 100"),
])
def test_get_human_age(input_cat_age: int,
                       input_dog_age: int,
                       expected_output: int
                       ) -> None:
    assert get_human_age(input_cat_age, input_dog_age) == expected_output
