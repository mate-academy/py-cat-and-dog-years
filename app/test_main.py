import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_to_animal",
    [
        pytest.param(-1, -1, [0, 0],
                     id="age can not be negative"),
        pytest.param(0, 0, [0, 0],
                     id="zero ages for pets the same for human"),
        pytest.param(14, 14, [0, 0],
                     id="not enough animals age for at least 1 human year"),
        pytest.param(15, 15, [1, 1],
                     id="15 years of cat/dog live gives 1 year of humans"),
        pytest.param(23, 23, [1, 1],
                     id="not enough cat/dog years to 2 humans years"),
        pytest.param(24, 24, [2, 2],
                     id="first 24 dog/cat years gives 2 humans years"),
        pytest.param(27, 27, [2, 2],
                     id="not enough cat/dog years to 3 humans years"),
        pytest.param(28, 28, [3, 2],
                     id="28 years of dogs live is not enough for"
                        " 3 humans years"),
        pytest.param(100, 100, [21, 17],
                     id="after first 24 years of dog/cat age"
                        " every 5 for dog and every 4 for cats lives"
                     " give 1 additional year for humans live"),
    ]
)
def test_function_returns_good_result(
        cat_age: int,
        dog_age: int,
        human_age_to_animal: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_to_animal


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ({1}, {1}),
        ([1], [2]),
        ((1,), (2,)),
        ({"cat": 2}, {"dog": 2}),
    ]
)
def test_age_pets_if_not_integer(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
