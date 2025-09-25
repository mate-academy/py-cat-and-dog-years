from app.main import get_human_age
import pytest
from typing import Union


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (13, 13, [0, 0]),
        (14, 14, [0, 0]),
        (-15, -1, [0, 0]),
        (15, 15, [1, 1]),
        (22, 22, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (26, 27, [2, 2]),
        (-27, -7, [0, 0]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
        (1000000, 1000000, [249996, 199997])
    ]
)
def test_animal_age_0_0_to_convert_human_age(
        cat_age: int,
        dog_age: int,
        result: list) -> None:
    res_age = get_human_age(cat_age, dog_age)
    assert res_age == result
    assert isinstance(res_age, list)
    assert len(res_age) == 2
    assert all(isinstance(v, int) for v in res_age)


@pytest.mark.parametrize("bad_input",
                         [
                             3.5,
                             "10",
                             None,
                             [1],
                             {"years": 10}
                         ]
                         )
def test_get_human_age_non_integer_type_raises(
        bad_input: Union[
            float,
            str,
            list,
            dict,
            None
        ]) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age=bad_input, dog_age=10)

    with pytest.raises(TypeError):
        get_human_age(10, dog_age=bad_input)
