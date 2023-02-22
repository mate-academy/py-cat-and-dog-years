import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,result",
                         [
                             (0, 14, [0, 0]),
                             (15, 23, [1, 1]),
                             (28, 23, [3, 1]),
                             (15, 29, [1, 3])
                         ]
                         )
def test_function_return_expected_values(cat_age: int,
                                         dog_age: int,
                                         result: list
                                         ) -> None:
    assert get_human_age(cat_age, dog_age) == result
