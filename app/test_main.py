import pytest
from app.main import get_human_age


def test_if_age_of_animals_less_15() -> None:
    cats_age = 14
    dogs_age = 14
    result = get_human_age(cats_age, dogs_age)
    assert result == [0, 0]


def test_is_it_working_propaly() -> None:
    result_1 = get_human_age(20, 32)
    get_human_age(19, 16)
    first_result = get_human_age(20, 32)

    assert result_1 == first_result


def test_if_age_of_animals_too_big() -> None:
    cats_age = 500
    dogs_age = 10982
    result = get_human_age(cats_age, dogs_age)
    assert result == [121, 2193]


def test_if_age_of_animals_less_0() -> None:
    cats_age = -25
    dogs_age = -18
    result = get_human_age(cats_age, dogs_age)
    assert result == [0, 0]


def test_if_arguments_is_not_integer() -> None:
    cats_age = {"k": 12}
    dogs_age = {"k": 10}

    with pytest.raises(TypeError):
        get_human_age(cats_age, dogs_age)


def test_if_age_of_animals_23() -> None:
    cats_age = 23
    dogs_age = 23
    result = get_human_age(cats_age, dogs_age)
    assert result == [1, 1]
