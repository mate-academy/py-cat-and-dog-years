import pytest
from typing import List, Union
from app.main import get_human_age


# Приклади з умови
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
        cat_age: int, dog_age: int,
        expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_return_contract_is_list_of_two_ints() -> None:
    result = get_human_age(15, 15)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


# Коти: поріг 15 (0->1)
@pytest.mark.parametrize(
    "cat_age, expected_cat",
    [
        (14, 0),  # just-before
        (15, 1),  # at
        (16, 1),  # just-after
    ],
)
def test_cat_boundary_first_year(cat_age: int, expected_cat: int) -> None:
    cat, dog = get_human_age(cat_age, 0)
    assert cat == expected_cat
    assert dog == 0


# Коти: поріг 24 (1->2)
@pytest.mark.parametrize(
    "cat_age, expected_cat",
    [
        (23, 1),
        (24, 2),
        (25, 2),
    ],
)
def test_cat_boundary_second_year(cat_age: int, expected_cat: int) -> None:
    cat, dog = get_human_age(cat_age, 0)
    assert cat == expected_cat
    assert dog == 0


# Коти: наступний крок кожні 4 роки (28 => 3)
@pytest.mark.parametrize(
    "cat_age, expected_cat",
    [
        (27, 2),
        (28, 3),
        (29, 3),
    ],
)
def test_cat_boundary_subsequent_steps(
        cat_age: int,
        expected_cat: int
) -> None:
    cat, dog = get_human_age(cat_age, 0)
    assert cat == expected_cat
    assert dog == 0


# Собаки: поріг 15 (0->1)
@pytest.mark.parametrize(
    "dog_age, expected_dog",
    [
        (14, 0),
        (15, 1),
        (16, 1),
    ],
)
def test_dog_boundary_first_year(dog_age: int, expected_dog: int) -> None:
    cat, dog = get_human_age(0, dog_age)
    assert cat == 0
    assert dog == expected_dog


# Собаки: поріг 24 (1->2)
@pytest.mark.parametrize(
    "dog_age, expected_dog",
    [
        (23, 1),
        (24, 2),
        (25, 2),
    ],
)
def test_dog_boundary_second_year(
        dog_age: int,
        expected_dog: int
) -> None:
    cat, dog = get_human_age(0, dog_age)
    assert cat == 0
    assert dog == expected_dog


# Собаки: наступний крок кожні 5 років (29 => 3)
@pytest.mark.parametrize(
    "dog_age, expected_dog",
    [
        (28, 2),  # just-before (24 + 5 - 1)
        (29, 3),  # at
        (30, 3),  # just-after
    ],
)
def test_dog_boundary_subsequent_steps(
        dog_age: int,
        expected_dog: int
) -> None:
    cat, dog = get_human_age(0, dog_age)
    assert cat == 0
    assert dog == expected_dog


# Негативні значення: клемпінг до нуля
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-5, -3, [0, 0]),
    ],
)
def test_negative_ages_are_clamped_to_zero(
        cat_age: int,
        dog_age: int,
        expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


# Дуже великі значення
def test_very_large_ages() -> None:
    one_million = 10**6
    assert get_human_age(one_million, one_million) == [249996, 199997]


# Float приймаються і обчислюються за правилами
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (3.5, 5.5, [0, 0]),
        (15.2, 23.8, [1, 1]),
        (24.0, 26.9, [2, 2]),
        (26.99, 27.0, [2, 2]),
    ],
)
def test_float_inputs_are_treated_as_years(
    cat_age: Union[int, float],
    dog_age: Union[int, float],
    expected: List[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


# Невалідні типи, що справді падають у поточній реалізації
@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 24),
        (24, "27"),
        (None, 10),
        ([], 5),
    ],
)
def test_invalid_types_raise_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
