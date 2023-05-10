import pytest

from app.main import get_human_age
from typing import NoReturn


@pytest.mark.parametrize(
    "cat_age,dog_age,human_result",
    [
        pytest.param(14, 14, [0, 0],
                     id="Check when cat's and dog's "
                        "age less than one human year"),
        pytest.param(15, 15, [1, 1],
                     id="Check when cat's and dog's"
                        " age is equal to one human year"),
        pytest.param(24, 24, [2, 2],
                     id="Check when cat's and dog's"
                        " age is equal to two human years"),
        pytest.param(28, 28, [3, 2],
                     id="Check one extra human year for cat"),
        pytest.param(100, 100, [21, 17],
                     id="Check extra human years for all animals")

    ]
)
def test_check_animal_age_for_human(cat_age: int, dog_age: int,
                                    human_result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_result


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        pytest.param(None, None, TypeError,
                     id="should return TypeError when animals ages is None"),
        pytest.param("", "", TypeError,
                     id="should return TypeError when animals ages is str"),
        pytest.param([], [], TypeError,
                     id="should return TypeError when animals ages is list"),
        pytest.param({0: 0}, {}, TypeError,
                     id="should return TypeError when animals ages is dict")
    ]
)
def test_should_raise_error(cat_age: int,
                            dog_age: int,
                            error: NoReturn) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
