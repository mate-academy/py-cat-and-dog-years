import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0,0,[0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24,24,[2, 2]),
        (28,28,[3, 2]),
        (100,100,[21, 17])
    ]
)

def test_convert_to_human_correctly(cat_age, dog_age, human_age):
    assert get_human_age(cat_age, dog_age) == human_age

@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(-5,4,ValueError,id="should raise error if data is negative"),
        pytest.param(0,-10,ValueError,id="should raise error if data is negative"),
        pytest.param(1000001,15,ValueError,id="should raise error if data is too large"),
        pytest.param(23,2000000,ValueError,id="should raise error if data is too large"),
        pytest.param(1.6,20,TypeError,id="should raise error if the function receives an incorrect type of data"),
        pytest.param(35,3.5,TypeError,id="should raise error if the function receives an incorrect type of data"),
        pytest.param("12",22,TypeError,id="should raise error if the function receives an incorrect type of data"),
        pytest.param(35,"55",TypeError,id="should raise error if the function receives an incorrect type of data")
    ]
)
def test_raising_errors_correctly(cat_age, dog_age, expected_error):
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
