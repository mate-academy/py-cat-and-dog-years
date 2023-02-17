import pytest

from app.main import get_human_age

# write your code here

get_human_age(0, 0) == [0, 0]
get_human_age(14, 14) == [0, 0]
get_human_age(15, 15) == [1, 1]
get_human_age(23, 23) == [1, 1]
get_human_age(24, 24) == [2, 2]
get_human_age(27, 27) == [2, 2]
get_human_age(28, 28) == [3, 2]
get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize(
    'cat_age,dog_age,result',
    [
        pytest.param(0, 0, [0, 0], id='animals are 0 years old'),
        pytest.param(14, 14, [0, 0], id='animals are 14 years old'),
        pytest.param(15, 15, [1, 1], id='animals are 15 years old'),
        pytest.param(23, 23, [1, 1], id='animals are 23 years old'),
        pytest.param(24, 24, [2, 2], id='animals are 24 years old'),
        pytest.param(27, 27, [2, 2], id='animals are 27 years old'),
        pytest.param(28, 28, [3, 2], id='animals are 28 years old'),
        pytest.param(100, 100, [21, 17], id='animals are 100 years old'),
    ]
)
def test_reasonable_values(cat_age: int,
                           dog_age: int,
                           result: list) -> None:
    assert (result == get_human_age(cat_age, dog_age))


@pytest.mark.parametrize(
    'cat_age,dog_age,result',
    [
        pytest.param(-1, -1, [0, 0], id='animals are -1 year old'),
        pytest.param(-314159265359, -314159265359, [0, 0],
                     id='animals age is huge negative integer'),
        pytest.param(314159265359, 314159265359, [78539816335, 62831853069],
                     id='animals age is huge positive integer'),
        pytest.param(-3.14159265359, -3.14159265359, [0, 0],
                     id='animals age is negative Pi'),
        pytest.param(3.14159265359, 3.14159265359, [0, 0],
                     id='animals age is Pi'),
    ]
)
def test_unreasonable_numbers(cat_age: int,
                              dog_age: int,
                              result: list) -> None:
    assert (result == get_human_age(cat_age, dog_age))


@pytest.mark.parametrize(
    'cat_age,dog_age',
    [
        pytest.param({1}, {1}, id='animals age is a dict'),
        pytest.param('1', '1', id='animals age is a string'),
        pytest.param(None, None, id='animals age is a None'),
    ]
)
def test_wrong_data_types(cat_age: int,
                          dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
