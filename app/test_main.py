import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,exp_cat,exp_dog",
    [
        (0, 0, 0, 0),  # базові нулі
        (14, 14, 0, 0),  # нижче першого порогу
        (15, 15, 1, 1),  # рівно перший поріг
        (23, 23, 1, 1),  # приклад з README
        (24, 24, 2, 2),  # рівно другий поріг
        (27, 27, 2, 2),  # усередині блоку
        (28, 28, 3, 2),  # кіт крокнув, собака ще ні
        (28, 29, 3, 3),  # собака крокнув на 29
        (100, 100, 21, 17),  # великі значення
        (15, 0, 1, 0),  # асиметричні
        (0, 15, 0, 1),
        (24, 15, 2, 1),
        (28, 23, 3, 1),
        (16, 0, 1, 0),  # перевірка округлення для кота
    ],
    ids=[
        "both_zero",
        "both_14",
        "both_15",
        "both_23",
        "both_24",
        "both_27",
        "cat_28_dog_28",
        "dog_steps_at_29",
        "large_100",
        "cat_15_dog_0",
        "cat_0_dog_15",
        "cat_24_dog_15",
        "cat_28_dog_23",
        "cat_16_rounding",
    ],
)
def test_get_human_age_parametrized(
    cat_age: int, dog_age: int, exp_cat: int, exp_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [exp_cat, exp_dog]
