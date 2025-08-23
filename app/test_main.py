import pytest
from app.main import get_human_age  # підкоригуй, якщо треба

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        # ... решта кейсів
    ],
)
def test_various_ages(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-3, -5),
        # ... інші негативні кейси
    ],
)
def test_negative_ages_raise_value_error(cat_age, dog_age) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("3", 5),
        (3, "5"),
        (3.5, 5),
        # ... інші неправильні типи
    ],
)
def test_invalid_types_raise_exception(cat_age, dog_age) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "age_before, age_after",
    [
        (14, 15),
        (23, 24),
        (27, 28),
        (29, 30),
    ],
)
def test_cat_monotonicity_at_thresholds(age_before, age_after) -> None:
    assert get_human_age(age_before, 30)[0] <= get_human_age(age_after, 30)[0]


# Аналогічно для собак

# І так далі — всі функції в одному файлі
