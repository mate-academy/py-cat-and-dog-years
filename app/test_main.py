import pytest

from app.main import get_human_age

# write your code here

@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(15, 15, [1,1], id="should convert first 15 years animals to 1 human"),
        pytest.param(24, 24, [2,2], id="should convert second 9 years animals to 1 human"),
        pytest.param(100, 100, [21,17], id="should convert every next 5 years for cat and 4 years for dog to 1 human"),
        pytest.param(23, 23, [1, 1], id="should convert discard the remainder"),
    ]
)
def test_can_sum(cat_age: int, dog_age: int, result: list) -> None:
   assert (get_human_age(cat_age,dog_age) == result)


