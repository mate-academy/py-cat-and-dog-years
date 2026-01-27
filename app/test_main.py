import pytest

from app.main import get_human_age

@pytest.mark.parametrize("cat_age,dog_age,result_conver",
                         [(0, 0, [0,0]),
                          (14, 14, [0, 0]),
                          (15 ,15, [1, 1]),
                          (23, 23, [1, 1]),
                          (24, 24, [2, 2]),
                          (27, 27, [2, 2]),
                          (28, 28, [3, 2]),
                          (100, 100, [21, 17]),
                          (-10, -10, [0, 0])
                          ])
def test_get_human_age(cat_age, dog_age, result_conver):
    assert get_human_age(cat_age, dog_age) == result_conver


def test_should_raise_type_error():
    with pytest.raises(TypeError):
        assert get_human_age("3","3")