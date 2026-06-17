from typing import Any
import pytest
from app.main import get_human_age


# --- TESTY PODSTAWOWE (z zadania) ---

@pytest.mark.parametrize(
    "cat_age, dog_age, exp_cat, exp_dog",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17),
    ]
)
def test_basic_examples(
    cat_age: int,
    dog_age: int,
    exp_cat: int,
    exp_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [exp_cat, exp_dog]


# --- TESTY GRANICZNE ---

@pytest.mark.parametrize(
    "cat_age, dog_age, exp_cat, exp_dog",
    [
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
    ]
)
def test_boundaries(
    cat_age: int,
    dog_age: int,
    exp_cat: int,
    exp_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [exp_cat, exp_dog]


# --- TESTY WARTOŚCI UJEMNYCH ---

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-10, -10),
    ]
)
def test_negative_values(cat_age: int, dog_age: int) -> None:
    # Funkcja nie ma walidacji, więc zwraca [0, 0]
    assert get_human_age(cat_age, dog_age) == [0, 0]


# --- TESTY NIEPOPRAWNYCH TYPÓW (rzucają TypeError) ---

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("abc", 10),
        (10, "xyz"),
        (None, 5),
        (5, None),
    ]
)
def test_invalid_types_raise_typeerror(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


# --- TESTY BARDZO DUŻYCH LICZB ---

def test_very_large_numbers() -> None:
    # kot: 1 + 1 + (10000 - 24) // 4 = 2496
    # pies: 1 + 1 + (10000 - 24) // 5 = 1997
    assert get_human_age(10000, 10000) == [2496, 1997]
