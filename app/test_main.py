import pytest
import app.main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Граничні значення для 0 людських років (менше 15 років тварини)
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),

        # Межа 1 людського року (рівно 15 років тварини)
        (15, 15, [1, 1]),

        # Граничні значення всередині 1 людського року (від 15 до 23)
        (23, 23, [1, 1]),

        # Межа 2 людських років (рівно 24 роки тварини)
        (24, 24, [2, 2]),

        # Перевірка проміжних значень перед наступним кроком (24 + 3 роки)
        (27, 27, [2, 2]),

        # Межа кроку для кота (24 + 4 = 28 років тварини -> 3 людські роки)
        # Собака при 28 роках все ще має 2 людські роки (бо крок 5)
        (28, 28, [3, 2]),

        # Межа кроку для собаки (24 + 5 = 29 років тварини -> 3 людські роки)
        (28, 29, [3, 3]),

        # Великі значення для перевірки формули на великій дистанції
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_boundaries(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    """Test get_human_age function with edge cases and boundaries."""
    assert app.main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Перевірка, що розрахунок для кота і собаки працює незалежно
        (15, 28, [1, 2]),
        (28, 15, [3, 1]),
        (0, 100, [0, 17]),
        (100, 0, [21, 0]),
    ]
)
def test_independent_aging_calculation(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    """Test that cat and dog ages are calculated independently."""
    assert app.main.get_human_age(cat_age, dog_age) == expected
