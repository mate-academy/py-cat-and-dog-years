import pytest
import app.main as main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_calculation(
    cat_age: int, dog_age: int, expected_result: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (30, 15, [3, 1]),
        (15, 30, [1, 3]),
        (28, 0, [3, 0]),
        (0, 29, [0, 3]),
        (32, 0, [4, 0]),
        (0, 34, [0, 4]),
    ]
)
def test_get_human_age_with_different_ages(
    cat_age: int, dog_age: int, expected_result: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "invalid_cat_age, invalid_dog_age, expected_exception",
    [
        (-1, 5, ValueError),      # Негативний вік кота
        (5, -1, ValueError),      # Негативний вік собаки
        (-10, -10, ValueError),   # Обидва віки негативні
        ("10", 5, TypeError),     # Вік кота - рядок
        (10, "5", TypeError),     # Вік собаки - рядок
        (12.5, 3, TypeError),     # Вік кота - float
        (10, 12.5, TypeError),    # Вік собаки - float
    ]
)
def test_get_human_age_invalid_input(
    invalid_cat_age, invalid_dog_age, expected_exception
) -> None:
    with pytest.raises(expected_exception):
        main.get_human_age(invalid_cat_age, invalid_dog_age)
