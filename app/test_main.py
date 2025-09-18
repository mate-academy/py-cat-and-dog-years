from app.main import get_human_age


import pytest

# =====================
# 1. Boundary-change tests
# =====================


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),  # до порога
    (15, 15, [1, 1]),  # на порозі
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_human_age_boundaries(cat_age: int,
                              dog_age: int,
                              expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

# =====================
# 2. Out-of-range / asymmetrical / zero tests
# =====================


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (0, 15, [0, 1]),
    (15, 0, [1, 0]),
    (-1, 10, [0, 0]),   # негативний кіт
    (10, -5, [0, 0]),   # негативна собака
    (10**6, 10**6, [249996, 199997]),  # дуже велике число (перевірка формули)
])
def test_human_age_out_of_range(cat_age: int,
                                dog_age: int,
                                expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

# =====================
# 3. Incorrect-type tests
# =====================


def test_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", 5)
    with pytest.raises(TypeError):
        get_human_age(None, 5)
    with pytest.raises(TypeError):
        get_human_age(2.5, 5)  # float кіт
    with pytest.raises(TypeError):
        get_human_age(5, 2.5)  # float собака

# =====================
# 4. Structural / type correctness
# =====================


def test_return_type_and_structure() -> None:
    result = get_human_age(28, 29)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
