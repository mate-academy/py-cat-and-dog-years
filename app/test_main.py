import pytest
from app.main import get_human_age

# Testes principais usando parametrização
@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (15, 24, [1, 2]),
        (24, 15, [2, 1]),
        (0, 20, [0, 2]),
        (20, 0, [2, 0]),
    ]
)
def test_get_human_age_valid_inputs(cat, dog, expected):
    assert get_human_age(cat, dog) == expected

# Testes de valores negativos — devem gerar ValueError
@pytest.mark.parametrize(
    "cat,dog",
    [
        (-1, 5),
        (5, -1),
        (-2, -3),
    ]
)
def test_get_human_age_negative_values(cat, dog):
    with pytest.raises(ValueError):
        get_human_age(cat, dog)

# Testes de tipos inválidos — devem gerar TypeError
@pytest.mark.parametrize(
    "cat,dog",
    [
        ("3", 2),
        (2, 5.5),
        (None, 2),
        (5, None),
        ([15], 20),
        (20, {"dog": 15}),
    ]
)
def test_get_human_age_invalid_types(cat, dog):
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
